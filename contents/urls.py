from django.urls import path, include
from  . import views

urlpatterns =[  
    path('content/<section>' , views.show_content),
    path('about/', views.show_about),
    path('contacts/',  views.show_contacts),
    path('policies/',  views.show_policies),
]