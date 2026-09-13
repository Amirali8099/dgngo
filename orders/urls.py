from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_view, name='cart'),
    path('add-to-order/', views.add_to_order, name='add_to_order'),
    path('user-panel/remove-order-detail', views.remove_order_detail, name='remove_order_detail'),
    path('user-panel/change-order-detail', views.change_order_detail, name='change_order_detail'),
    path('checkout/', views.checkout_cart, name='checkout_cart'),
    path('panel/', views.panel_view, name='panel'),
]
