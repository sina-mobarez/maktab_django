from django.urls import path

from rental import views

urlpatterns = [
    path('', views.list_actors),
]
