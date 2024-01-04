from django.contrib import admin
from .models import T


class TAdmin(admin.ModelAdmin):
    list_display = ('name','price','quantity')




admin.site.register(T, TAdmin)
