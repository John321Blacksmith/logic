"""online_market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    # api endpoint initial for the diary store
    path('api/v1/diary/', include('diary.urls')),

    # api endpoint initial for the grocery store
    path('api/v1/grocery/', include('grocery.urls')),

    # api endpoint initial for the butchers store
    path('api/v1/butchers/', include('butchers.urls')),

    # api endpoint initial for the bakery store
    path('api/v1/bakery/', include('bakery.urls')),
    
    # the user oriented api endpoints
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
]
