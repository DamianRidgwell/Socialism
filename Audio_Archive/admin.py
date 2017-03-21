from django.contrib import admin

# Register your models here.
from .models import Talk, Speaker, Category, Conference, TimeSlot, Day

admin.site.register(Talk)
admin.site.register(Speaker)
admin.site.register(Category)
admin.site.register(Conference)
admin.site.register(TimeSlot)
admin.site.register(Day)
