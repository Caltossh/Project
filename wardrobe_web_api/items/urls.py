from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.ItemView.as_view()),
    path('items/<int:id>/', views.ItemDetailView.as_view()),
    path('items/<int:id>/photos', views.ItemPhotosAPIView.as_view()),
]