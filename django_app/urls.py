"""django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from contents import views as content_views
from . import settings
from paypal.standard.ipn import urls as paypal_urls

urlpatterns = [
    path('', content_views.show_home , name='home' ),
    path('ck_uploads/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('about/', include('contents.urls')),
    path('products/', include('products.urls') ),
    path('accounts/', include('accounts.urls') ),
    path('shopping/', include('shopping.urls') ),
    path('paypal/', include(paypal_urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)