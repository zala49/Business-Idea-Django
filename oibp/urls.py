from django.contrib import admin
from django.urls import path, include
from customer import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myadmin/', include('myadmin.urls')),
    path('innovator/', include('innovator.urls')),
    path('customer/', include('customer.urls')),
    path('', views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)