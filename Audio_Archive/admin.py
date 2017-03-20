from django.contrib import admin

# Register your models here.
from .models import Talk, Speaker, Category

admin.site.register(Talk)
admin.site.register(Speaker)
admin.site.register(Category)
