from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from web.models import Todo

test_1 = 1
test_2 = 0


def index(request):
    context = {
        'title': 'function based view',
    }

    return render(request, 'index.html', context)


class TestView(views.View):
    def get(self, request):
        context = {
            'title': 'class based view',
        }

        return render(request, 'index.html', context)

    def post(self, request):
        pass


class IndexTemplateView(views.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Class based with template view'

        return context


class RedirectToIndexView(views.RedirectView):
    url = reverse_lazy('index cbv')

    def get_redirect_url(self, *args, **kwargs):
        if test_1 > test_2:
            return 1
        else:
            return 0


class TodosListViews(views.ListView):
    model = Todo
    template_name = 'todos-list-view.html'
    ordering = ('title', 'category__name')
    context_object_name = 'todos'

    def get_queryset(self):
        queryset = super().get_queryset()

        title_filter = self.request.GET.get('filter', None)
        if title_filter:
            queryset = queryset.filter(title__contains=title_filter)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'My todos'

        return context


class TodoDetailsView(views.DetailView):
    model = Todo
    template_name = 'todo-details.html'


class TodoCreateView(views.CreateView):
    model = Todo
    template_name = 'todo-create.html'
    success_url = reverse_lazy('todos list')
    fields = '__all__'


# class PetDetails(views.DetailView):
#     model = Pet
#     template_name = 'xxx'