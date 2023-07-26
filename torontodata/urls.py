"""torontodata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from basicmap import views

router = routers.DefaultRouter()
router.register(r'washroomdata', views.WashroomDataView, basename='washroomdata')

urlpatterns = [
    # path("", include("basicmap.urls")),
    # path("basicmap/", include("basicmap.urls")),
    # path("admin/", admin.site.urls),
    # path('api/', include(router.urls)),

    # Note: The nginx config file is set up so that the django backend is served through
    # address.com/api. Therefore, this path (and the entire backend) is accessable
    # only through address.com/api. The frontend will be served through another path
    # with React.
    path('/', include(router.urls))
]


"""
nginx config
Edit via sudo vi /etc/nginx/sites-available/torontodata

server {
    listen 80;
    server_name 35.183.91.143;

    location /api {
        include proxy_params;
        proxy_pass http://localhost:8000/;
    }

    location / {
        include proxy_params;
        proxy_pass http://localhost:8000/;
    }
}

"""
