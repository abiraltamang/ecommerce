from django.urls import path, include
from shopping import views

urlpatterns = [
    path('add_to_wishlist/<pid>', views.add_to_wishlist, name='aw' ),
    path('add_to_cart/<pid>/<qty>', views.add_to_cart,name='ac' ),
    path('remove_from_wishlist/', views.remove_from_wishlist, name='rw' ),
    path('remove_from_cart/', views.remove_from_cart, name='rc' ),
    path('checkout/', views.checkout, name='checkout' ),
    path('comment/', views.comment, name='comment'),
    path('review/', views.comment, name='review' ),
]