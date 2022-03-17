from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('menupage',views.menupage,name="menupage"),
    path('about',views.about,name="about"),
    path('cart', views.cart, name="cart"),
    path('signup',views.signup,name="signup"),
    path('login',views.customerLogin,name="login"),
    path('logout', views.handelLogout, name="handleLogout"),
    path('post_product', views.post_product, name="post_product"),
    path('remove_item', views.remove_item, name="remove_item"),
    path('check_out', views.check_out, name="check_out"),
    path('orders', views.orders, name="orders"),
]