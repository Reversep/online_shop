from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
   openapi.Info(
      title="Online shop API",
      default_version='v0.0.1',
      description="API documentation for Online Shop KG",
      contact=openapi.Contact(email="codify@gmail.com"),
      license=openapi.License(name="NO LICENCE"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

doc_urlpatterns = [
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('items.urls'))
] + doc_urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

