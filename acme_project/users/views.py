# from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from users.forms import CustomUserCreationForm
from users.models import CustomUser


class UserCreateView(CreateView):
    model = CustomUser
    template_name = 'registration/registration_form.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('pages:homepage')
