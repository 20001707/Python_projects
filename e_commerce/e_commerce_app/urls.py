from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('slogin/',slogin),
    path('sregister/',sregister),
    path('profile/',seller_profile),
    path('upload/',upload),
    path('edit_profile/<int:id>',edit_profile),
    path('view_product/<int:id>',seller_productview),
    path('userreg/',userregister),
    path('userlog/',userlogin),
    path('userprofile/',user_profile),
    path('userindex_all/',userindex),
    path('userindex/<category>',userindex_category),
    path('wishlist/<int:id>',wishlist),
    path('wishview/',wishlist_view),
    path('delete_wish/<int:id>',delete_wish),
    path('cart_add/<int:id>',cart_add),
    path('cart_view/',cart_view),
    path('cartinc/<int:id>',cartinc),
    path('cartdec/<int:id>',cartdec),
    path('cart_delete/<int:id>',cart_delete),
    path('user_address/',user_address),
    path('edit_useraddress/',edit_useraddress),
    path('payment/',payment),
    path('orderdetails/',order_details),
    # path('user_logout/',user_logout),
    

    
    
    
]