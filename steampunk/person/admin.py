from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
    list_display_links = ('name',)
    search_fields = ('name', 'level')

# Register your models here.
admin.site.register(Person, PersonAdmin)
