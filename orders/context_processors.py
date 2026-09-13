# def cart_count(request):
#
#     if request.user.is_authenticated:
#         from .models import Order
#         cart = Order.objects.filter(user=request.user, is_ordered=False).first()
#         if cart:
#             return {'header_cart_count': cart.total_count}
#     return {'header_cart_count': 0}
