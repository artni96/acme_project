from django.urls import path
from users.views import UserCreateView


urlpatterns = [
    path('registration/', UserCreateView.as_view(), name='registration')
]
