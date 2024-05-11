from django.urls import path

from .import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('product/',views.product_list,name='product'),
    # path('cart/',views.cart_details,name='cart'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
]
