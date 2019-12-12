from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from parts.views import ClientView
from .views import *

app_name = "parts"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('clients/', ClientView.as_view()),
    url(r'verify/', AttendanceView.as_view({'post': 'verify'}), name='verify'),
]
urlpatterns = format_suffix_patterns(urlpatterns)