from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path("admin/", admin.site.urls),
    path("user/", include("auth_app.urls")),
    path('account/', include('allauth.urls')),
    path("", include("main_app.urls")),
    path("blog/", include("blog_app.urls", namespace="blog_app")),
    path("qa/", include("qa_app.urls")),
    path("shop/", include("shop_app.urls", namespace="shop_app")),
    path("cart/", include("cart_app.urls", namespace="cart_app")),
    path("orders/", include("orders_app.urls", namespace="orders_app")),
    path("payment/", include("payment_app.urls", namespace="payment_app")),
    path("voice/", include("voice_app.urls", namespace="voice_app")),
    path("monitoring/", include("monitoring_app.urls", namespace = 'monitoring_app')),
    path("terms/", include("main_app.urls")),
    path("management/", include("management_app.urls", namespace = 'management_app')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
