from django.contrib.admin.sites import site
from crudajax.views import CrudUser
from django.contrib import admin
from .models import CrudUser
# Register your models here.

admin.site.register(CrudUser)