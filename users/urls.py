from django.urls import path
from . import views


urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('create/recipe', views.create_recipes, name='create_recipes'),
    path('delete/<int:recipes_id>', views.delete_recipes, name='delete_recipes'),
    path('edit/<int:recipes_id>', views.edit_recipes, name='edit_recipes'),
    path('update', views.update_recipes, name='update_recipes'),
]
