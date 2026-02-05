from django.contrib import admin

from rental import models
# Register your models here.

admin.site.register(models.Actor)
admin.site.register(models.Film)

