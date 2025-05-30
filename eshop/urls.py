from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from apps.products.views import (home, product_detail, male_products, content,
                                  female_products, category_detail, contact,  cart_update,
                                   search_view, faq, cart_add, cart_remove, 
                                  cart_detail, checkout_view, cart_add_ajax, cart_remove_ajax)
from apps.users.views import (login_view, reg_view, 
                               logout_view, profile_view)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
    path('content/', content, name='content'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('register/', reg_view, name='register'),
    path('search/', search_view, name='search'),
    path('checkout/', checkout_view, name='checkout'),  
]
urlpatterns += i18n_patterns(
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('profile/', profile_view, name='profile'),
    path('products/male/', male_products, name='male_products'),
    path('products/female/', female_products, name='female_products'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
    path('faq/', faq, name='faq'),
    path('cart/', cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', cart_remove, name='cart_remove'),
    path('cart/update/<int:product_id>/', cart_update, name='cart_update'),
    path('cart/add/ajax/', cart_add_ajax, name='cart_add_ajax'),
    path('cart/remove/ajax/', cart_remove_ajax, name='cart_remove_ajax'),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
