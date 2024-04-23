from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.ItemView.as_view()),
    path('items/<int:id>/', views.ItemDetailView.as_view()),
    path('items/<int:id>/photos/', views.item_photos),
    path('categories/', views.CategoryView.as_view()),
    path('categories/<int:id>/', views.CategoryDetailView.as_view()),
    path('categories/<int:id>/items/', views.category_items, name='category_items'),
]