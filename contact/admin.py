# type: ignore

from django.contrib import admin
from contact import models

# Register your models here.


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'id',


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'email', 'show',
    ordering = 'first_name',
    list_filter = 'created_date',
    list_per_page = 25
    list_max_show_all = 200
    list_editable = 'phone', 'show',
    list_display_links = 'first_name', 'last_name',
    search_fields = 'id', 'first_name', 'last_name'
