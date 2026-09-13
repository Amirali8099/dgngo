from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from .models import Product, Category, ProductReview


def product_list(request):
    products = Product.objects.filter(is_available=True)

    category_slug = request.GET.get('category')
    if category_slug:
        products = products.filter(category__slug=category_slug)

    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
        'page_obj': page_obj,
        'paginator': paginator,
        'categories': Category.objects.all(),
    }
    return render(request, 'products/product_list.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_available=True)
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)


def submit_review(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        comment = request.POST.get('comment', '').strip()
        email = request.POST.get('email', '').strip()
        rating = request.POST.get('rating') or 5

        if name and comment:
            ProductReview.objects.create(
                product=product,
                name=name,
                email=email,
                rating=int(rating),
                comment=comment,
            )

    return redirect(product.get_absolute_url() + '#product-tab-reviews')
