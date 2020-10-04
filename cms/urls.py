from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('category/<int:cat_id>/', views.category, name='category'),
    path('create-post/', views.add_post, name='add_post'),
    path('update-post/<int:post_id>', views.update_post, name='update_post'),
    path('view-post/<int:post_id>', views.view_post, name='view_post'),
    path('delete-post/<int:post_id>', views.delete_post, name='delete_post'),
]
