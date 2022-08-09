from django.contrib import admin
from .models import Recipes


class ListingRecipes(admin.ModelAdmin):
    list_display = ('id', 'recipe_name', 'category')
    list_display_links = ('id', 'recipe_name')
    search_fields = ('recipe_name', 'id')
    list_filter = ('category',)


admin.site.register(Recipes, ListingRecipes)
