"""
URL configuration for ecoway_finder project.

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
from django.urls import include, path

from trips import urls as trips_urls
from users import urls as users_urls
from cars import urls as cars_urls
from trips import views as trips_views
from users import views as users_views
from passengers import urls as passengers_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/login/', users_views.login, name='login'),
    path('users/', include(users_urls)),
    path('trips/', include(trips_urls)),
    path('cars/', include(cars_urls)),
    path('addresses/<int:pk>/', trips_views.AddressApiView.as_view()),
    path('addresses/', trips_views.AddressChangeApiView.as_view()),
    path('passengers/', include(passengers_urls)),
]
