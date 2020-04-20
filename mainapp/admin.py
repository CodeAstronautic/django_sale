from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import *

# Register your models here.
admin.site.register(get_user_model())
admin.site.register(AddProduct)
admin.site.register(Category)
admin.site.register(AddPrice)