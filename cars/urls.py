from django.urls import include, path
from . import views as cars_views

urlpatterns = [
    path('<int:pk>/', cars_views.CarApiView.as_view()),
    path('', cars_views.CarChangeApiView.as_view()),
]
