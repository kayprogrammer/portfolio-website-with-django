from django.contrib import admin
from . models import *

# Register your models here.

MyModels = [About, Work, Skill, Portfolio, Contact]

admin.site.register(MyModels)