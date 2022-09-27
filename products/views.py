from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpResponseNotFound
from .models import Product, Reservation, Review
from django.contrib.auth.models import User
from .forms import ProductForm, DateForm, ReviewForm
from datetime import datetime


def all_products(request):

    products = Product.objects.all()
    query = None

    if request.GET:
        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter \
                    any search criteria!")
                return redirect(reverse("products"))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        "products": products,
        "search_term": query,
    }

    return render(request, "products/products.html", context)


def is_service_products(request):

    products = Product.objects.filter(is_service=True)
    query = None

    if request.GET:
        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter any \
                    search criteria!")
                return redirect(reverse("products"))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        "products": products,
        "search_term": query,
    }

    return render(request, "products/is_service_products.html", context)


def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        "product": product,
    }

    return render(request, "products/product_detail.html", context)


@login_required
def add_product(request):
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request, "Failed to add product. Please ensure \
                    the form is valid."
            )
    else:
        form = ProductForm()

    template = "products/add_product.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request, "Failed to update product. Please \
                    ensure the form is valid."
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.name}")

    template = "products/edit_product.html"
    context = {
        "form": form,
        "product": product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, "Product deleted!")
    return redirect(reverse("products"))


def user_is_barber(request):
    if request.GET and "service-id" in request.GET:
        service_id = request.GET["service-id"]
    else:
        return HttpResponseNotFound()
    service = get_object_or_404(Product, pk=service_id, is_service=True)

    barbers = User.objects.filter(groups__name="Barber")

    context = {
        "barbers": barbers,
        "service": service,
    }

    return render(request, "products/barbers.html", context)


def get_qs_param(request, param_name):
    if request.GET and param_name in request.GET:
        return request.GET[param_name]
    raise ValueError()


def booking_form(request):
    current_user = request.user
    try:
        service_id = get_qs_param(request, "service-id")
        barber_id = get_qs_param(request, "barber-id")
        barber = User.objects.get(pk=barber_id)
        service = Product.objects.get(pk=service_id, is_service=True)
    except (ValueError, ObjectDoesNotExist):
        return HttpResponseNotFound()

    if request.method == "GET":
        form = DateForm()
        context = {
            "form": form,
            "service": service,
            "barber": barber,
        }
        return render(request, "products/booking_form.html", context)

    elif request.method == "POST":
        form = DateForm(request.POST)
        if form.is_valid():
            time = form.cleaned_data["time_choice"]
            date = form.cleaned_data["date"]
            dt = datetime.combine(date, time)
            reservation = Reservation.objects.create(
                date_time=dt, barber=barber, product=service, user=current_user
            )
            context = {"reservation": reservation}
            return render(request, "products/booking_success.html", context)
        context = {
            "form": form,
            "service": service,
            "barber": barber,
        }
        return render(request, "products/booking_form.html", context)
