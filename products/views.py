from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseNotFound
from .models import Product
from django.contrib.auth.models import User, Group
from .forms import ProductForm, DateForm


def all_products(request):

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def is_service_products(request):

    products = Product.objects.filter(is_service=True)
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/is_service_products.html', context)


def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
        
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


def user_is_barber(request):

    # Get service ID from QS params. If not sevice ID in QS params or serive does not exist, show 404

    # Check if search param exists
    # If it exists, assign to variable
    # If not, return 404
    # Try to get the service or 404
    # Add service to context

    if request.GET and 'service-id' in request.GET:
        service_id = request.GET['service-id']
    else:
        return HttpResponseNotFound()
    service = get_object_or_404(Product, pk=service_id, is_service=True)

    barbers = User.objects.filter(groups__name='Barber')

    context = {
        'barbers': barbers,
        'service': service,
    }

    return render(request, 'products/barbers.html', context)


def booking_form(request):

    # Check if sevice search param exists
    # If it exists, assign to variable
    # If not, 404
    # Check if barber search param exists
    # If it exists, assign to variable
    # If not, 404
    # Try to get the service or 404
    # Try to get the barber or 404
    # Add service and barber to context
    # Render title 'pick a time for your product.name with barber.name'

    if request.GET and 'service-id' in request.GET:
        service_id = request.GET['service-id']
    else:
        return HttpResponseNotFound()

    if request.GET and 'barber-id' in request.GET:
        barber_id = request.GET['barber-id']
    else:
        return HttpResponseNotFound()
    barber = get_object_or_404(User, pk=barber_id)
    service = get_object_or_404(Product, pk=service_id, is_service=True)

    form = DateForm(request.POST)

    context = {
        'form': form,
        'service': service,
        'barber': barber,

    }

    return render(request, 'products/booking_form.html', context)


