from django.urls import path
from . import views

urlpatterns = [
    path('shows/', views.show_products, name='product_show' ),
    path('search/<key', views.searched_products, name= 'searched_products'),
    path('classified/<genre>/<value>',views.classified_products, name="classified_products"),
    path('details/<int:id>', views.show_product_details, name='product_detail')
]