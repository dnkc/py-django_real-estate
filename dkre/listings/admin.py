from django.contrib import admin

# Register your models here.

# where you customize admin stuff for listings app
from .models import Listing

admin.site.register(Listing)