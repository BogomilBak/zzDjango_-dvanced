from django.urls import path
from web.views import *
urlpatterns = (
    path('create/', ProfileCreateView.as_view(), name='create profile'),
    path('', ProfileListView.as_view(), name='list profiles'),
    path('<int:pk>/', ProfileDetailsView.as_view(), name='details profile'),
)