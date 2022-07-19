from django.urls import path

from . import views

urlpatterns = [
    path('', views.display_curr_time, name="display current time"),
]