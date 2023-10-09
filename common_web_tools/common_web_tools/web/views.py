import random

from django.core.cache import cache
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views import generic as views

from common_web_tools.web.models import Profile


# @cache_page(15)
def show_index(request):
    Profile.objects.create(
        name='Bogi',
        email='Bogi@bogi.it'
    )

    profiles = Profile.objects.all()

    if not cache.get('value2'):
        value_2 = random.randint(1, 1024)
        cache.set('value2', value_2, 30)

    count = request.session.get('count') or 0
    request.session['count'] = count + 1

    paginator = Paginator(profiles, per_page=5)
    current_page = request.GET.get('page', 1)

    context = {
        'value': random.randint(1, 1024),
        'value2': cache.get('value2'),
        'count': request.session.get('count'),
        'profiles': profiles,
        'profiles_page': paginator.get_page(current_page),
    }

    return render(request, 'index.html', context)


def show_book_details(request, pk):
    last_viewed = request.session.get('last_viewed_books', [])
    last_viewed.append(pk)
    request.session['last_viewed_books'] = last_viewed


class ProfilesListView(views.ListView):
    model = Profile
    template_name = 'profiles.list.html'
    paginate_by = 3

    # def get_paginate_by(self, queryset):
    #     return self.request.GET.get('pages_count', 1)