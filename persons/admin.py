from django.contrib import admin
from .models import Person


class ListingPersons(admin.ModelAdmin):
    list_display = ('id', 'person_name', 'person_email')
    list_display_links = ('id', 'person_name')
    search_fields = ('id', 'person_name',)


admin.site.register(Person)
