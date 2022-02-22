from django.contrib import admin
from .models import Data
# Register your models here.


class DataAdmin(admin.ModelAdmin):
    fields = ("name","title","phone_number")
admin.site.register(Data,DataAdmin)
