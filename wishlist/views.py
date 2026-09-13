from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from products.models import Product
from .models import WishlistItem


@login_required(login_url='login_page')
def wishlist_view(request):
    items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'wishlist/wishlist.html', {'items': items})


@login_required(login_url='login_page')
def toggle_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    item = WishlistItem.objects.filter(user=request.user, product=product).first()

    if item:
        item.delete()
    else:
        WishlistItem.objects.create(user=request.user, product=product)

    return redirect(request.META.get( 'wishlist'))


# Create your views here.
