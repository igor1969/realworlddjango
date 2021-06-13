from django.contrib import admin

from .models import Category, Event


@admin.register(Event)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class BrandAdmin(admin.ModelAdmin):
    pass


