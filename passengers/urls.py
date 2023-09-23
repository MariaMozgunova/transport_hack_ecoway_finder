from django.urls import include, path
from . import views as passengers_views

urlpatterns = [
    path('<int:pk>/', passengers_views.PassengerApiView.as_view()),
    path('', passengers_views.PassengerChangeApiView.as_view()),
    path('groups/<int:pk>/', passengers_views.PassengerGroupApiView.as_view()),
    path('groups/', passengers_views.PassengerGroupChangeApiView.as_view()),
]
