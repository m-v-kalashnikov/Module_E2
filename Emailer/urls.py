from django.urls import path
from .views import *

app_name = 'Emailer'
urlpatterns = [
    path('', index, name='main'),
    path('detail/', detail_page, name='detail'),
]
