from django.contrib import admin
from django.urls import path
from apps.products.views import home, product_detail, category_detail, contact, content
from apps.users.views import login_view, reg_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
    path('content/', content, name='content'),
    path('login/', login_view, name='login'),
    path('register/', reg_view, name='register'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
