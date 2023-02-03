from django.urls import path
from . import views
urlpatterns=[
    path('cart_details',views.cart_details,name='cart_details'),
    path('add_cart/<int:product_id>/',views.add_cart,name='add_cart'),
    path('cart_decrement/<int:product_id>/',views.min_cart,name='cart_decrement'),
    path('remove/<int:product_id>/',views.cart_delete,name='remove'),
    path('logout/',views.logout,name='logout'),
    
]