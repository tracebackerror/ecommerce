from django.urls import path
from .views import *

urlpatterns = [
    path('login/',CustomLoginView.as_view()),
    path('register/',CustomRegistrationView.as_view()),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('logout/',custom_logout),
    path('address/delete/<int:address_id>/',deleteAddress),
]