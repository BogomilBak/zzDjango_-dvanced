from django.urls import path

from common_web_tools.web.views import show_index, ProfilesListView

urlpatterns = [
    path('', show_index, name='index'),
    path('profiles/', ProfilesListView.as_view(), name='profiles list'),
]

import common_web_tools.web.signals