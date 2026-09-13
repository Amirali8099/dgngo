from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from products.models import Product
from .models import Order, OrderDetail


def get_cart(user):
    """سبد خرید فعلی کاربر (سفارشی که هنوز نهایی نشده) را برمی‌گرداند یا می‌سازد."""
    cart, _ = Order.objects.get_or_create(user=user, is_ordered=False)
    return cart


@login_required(login_url='login_page')
def cart_view(request):
    cart = get_cart(request.user)
    return render(request, 'orders/cart.html', {'cart': cart})


def add_to_order(request):
    if not request.user.is_authenticated:
        return JsonResponse({
            'status': 'not_logged_in',
            'icon': 'warning',
            'text': 'برای افزودن به سبد خرید ابتدا وارد حساب کاربری خود شوید.',
            'confirm_button_text': 'ورود به حساب',
        })

    product_id = request.GET.get('product_id')
    count = int(request.GET.get('count', 1))
    product = get_object_or_404(Product, id=product_id)

    cart = get_cart(request.user)
    detail, created = OrderDetail.objects.get_or_create(order=cart, product=product)
    if not created:
        detail.count += count
    else:
        detail.count = count
    detail.save()

    return JsonResponse({
        'status': 'success',
        'icon': 'success',
        'text': f'"{product.title}" به سبد خرید اضافه شد.',
        'confirm_button_text': 'باشه',
    })


@login_required(login_url='login_page')
def remove_order_detail(request):
    detail_id = request.GET.get('detail_id')
    detail = get_object_or_404(OrderDetail, id=detail_id, order__user=request.user)
    detail.delete()

    cart = get_cart(request.user)
    body = render_to_string('orders/_cart_items.html', {'cart': cart}, request=request)
    return JsonResponse({'status': 'success', 'body': body})


@login_required(login_url='login_page')
def change_order_detail(request):
    detail_id = request.GET.get('detail_id')
    state = request.GET.get('state')
    detail = get_object_or_404(OrderDetail, id=detail_id, order__user=request.user)

    if state == 'increase':
        detail.count += 1
        detail.save()
    elif state == 'decrease':
        detail.count -= 1
        if detail.count < 1:
            detail.delete()
        else:
            detail.save()

    cart = get_cart(request.user)
    body = render_to_string('orders/_cart_items.html', {'cart': cart}, request=request)
    return JsonResponse({'status': 'success', 'body': body})


@login_required(login_url='login_page')
def checkout_cart(request):
    cart = get_cart(request.user)
    if cart.details.exists():
        cart.is_ordered = True
        cart.save()
    return redirect('panel')


@login_required(login_url='login_page')
def panel_view(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', '').strip()
        user.last_name = request.POST.get('last_name', '').strip()
        user.email = request.POST.get('email', '').strip()

        new_password = request.POST.get('new_password', '').strip()
        if new_password:
            user.set_password(new_password)

        user.save()

        if new_password:
            return redirect('login_page')

    orders = request.user.orders.filter(is_ordered=True)
    return render(request, 'orders/panel.html', {'orders': orders})


# Create your views here.
