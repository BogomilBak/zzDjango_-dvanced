from django.urls import path, include

from web.views import TestView, index, IndexTemplateView, TodosListViews, TodoDetailsView, TodoCreateView

urlpatterns = [
    path('cbv', TestView.as_view(), name='index cbv'),
    path('', index, name='index function based view'),
    path('cbv-template/', IndexTemplateView.as_view(), name='index cbv - template'),
    path('todos-list/', TodosListViews.as_view(), name='todos list'),
    path('todos/<int:pk>/', TodoDetailsView.as_view(), name='todo details'),
    path('todos/create/', TodoCreateView.as_view(), name='create todo'),
]