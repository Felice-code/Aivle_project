from django.shortcuts import render, get_object_or_404, redirect
from cart_app.forms import CartAddProductForm
from .models import Category, Product
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    recent_products_ids = request.session.get('recent_products', [])
    recent_products = Product.objects.filter(id__in=recent_products_ids)

    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'recent_products': recent_products})

@login_required
def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    stock_alert = product.stock <= 10

    # 최근 본 상품에 추가
    recent_products = request.session.get('recent_products', [])
    if product.id not in recent_products:
        recent_products.append(product.id)
        request.session['recent_products'] = recent_products

    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'stock_alert': stock_alert})

@login_required
def add_to_recent_products(request, id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=id, available=True)
        recent_products = request.session.get('recent_products', [])
        if product.id not in recent_products:
            recent_products.append(product.id)
            request.session['recent_products'] = recent_products
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'}, status=400)


@login_required
def remove_from_recent_products(request, id):
    recent_products = request.session.get('recent_products', [])
    if id in recent_products:
        recent_products.remove(id)
        request.session['recent_products'] = recent_products
    return redirect('shop_app:product_list')