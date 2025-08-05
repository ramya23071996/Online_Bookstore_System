from django.urls import path
from . import views

urlpatterns = [
    path('author/<int:author_id>/', views.author_books, name='author_books'),
    path('category/<int:category_id>/', views.category_books, name='category_books'),
    path('', views.home, name='home'),

]