from django.contrib import admin
from .models import Country , State
# Register your models here.


@admin.register(Country)
class CountryAdmin (admin.ModelAdmin):
    list_display = ('name', 'created_date',)
    list_display_links = ('name', 'created_date',)


@admin.register(State)
class StateAdmin (admin.ModelAdmin):
    list_display = ('country', 'province','created_date',)
    list_display_links = ('country','province', 'created_date',)