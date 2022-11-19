from django.contrib import admin
from .models import *
# Register your models here.

class kolomKaryawan(admin.ModelAdmin):
    list_display = ['full_name', 'emp_code','phone', 'email','birth_place', 'birth_day', 'position_id', 'create_at']
    search_fields= ['emp_code', 'full_name']
    list_filter = ('position_id')
    list_per_page = 3

admin.site.register(Karyawan)
admin.site.register(Position)