from django.urls import include, path
from . import views as trips_views

urlpatterns = [
    path('<int:pk>/', trips_views.TripApiView.as_view()),
    path('', trips_views.TripChangeApiView.as_view()),
]
