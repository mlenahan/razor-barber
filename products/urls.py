from django.urls import path
from django.views.i18n import JavaScriptCatalog
from . import views

urlpatterns = [
    path("", views.all_products, name="products"),
    path("services/", views.is_service_products, name="services"),
    path("barbers/", views.user_is_barber, name="barbers"),
    path("booking/", views.booking_form, name="booking"),
    path("booking-failure/", views.booking_failure, name="booking_failure"),
    path("jsi18n", JavaScriptCatalog.as_view(), name="js-catalog"),
    path("<int:product_id>/", views.product_detail, name="product_detail"),
    path("add/", views.add_product, name="add_product"),
    path("edit/<int:product_id>/", views.edit_product, name="edit_product"),
    path("delete/<int:product_id>/", views.delete_product,
         name="delete_product"),
]
