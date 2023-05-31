from django.urls import path
from .views import *

urlpatterns = [
    path('login/',CustomLoginView.as_view()),
    path('register/',CustomRegistrationView.as_view()),
    path('logout/',custom_logout),
]