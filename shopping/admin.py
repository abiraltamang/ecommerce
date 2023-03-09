from django.contrib import admin
from shopping.models import *

# Register your models here.

admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Comment)
admin.site.register(Review)
