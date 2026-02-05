from django.shortcuts import render

from rental import models as rental_models

# Create your views here.


def list_actors(request):
    actors = rental_models.Actor.objects.filter(first_name__contains='ce')
    return render(request, 'index.html', {'actors': actors})