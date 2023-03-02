from django.urls import path, include
from  . import views

urlpatterns =[  
    path('intro/', views.show_intro),
    path('contacts/',  views.show_contacts),
    path('policies/',  views.show_policies),
]