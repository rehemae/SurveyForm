from django.urls import include, path

from survey import admin

urlpatterns = [
    # Constracting routing configuration
  path('admin/', admin.site.urls),
  path('api/',include('api.urls')),]

