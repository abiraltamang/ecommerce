from django.urls import path
from . import views

urlpatterns = [
    path('shows/', views.show_products ),
    path('details/<int:id>', views.show_product_details)
]