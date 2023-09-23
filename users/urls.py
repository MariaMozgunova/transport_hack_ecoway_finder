from django.urls import include, path
from . import views as users_views

urlpatterns = [
    path('register/', users_views.UserCreateApiView.as_view()),
    path('<int:pk>/', users_views.UserApiView.as_view()),
]
