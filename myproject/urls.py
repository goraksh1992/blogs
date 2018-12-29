from django.contrib import admin
from django.urls import path
import blogs.views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogs.views.home, name='home'),

] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
