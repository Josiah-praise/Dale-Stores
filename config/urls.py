from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index-page'),
    path('admin/', admin.site.urls),
    path('accounts/', include('account.urls', "account")),
    path('store/', include('store.urls', "store")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
