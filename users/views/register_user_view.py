from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import RegisterUserForm
from users.utils import get_token
from django.contrib.auth import get_user_model


User = get_user_model()


def register_user_view(request):
    """Функция регистрации пользователя."""
    if request.method == 'POST':
        form = RegisterUserForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False) 
            user.is_superuser = False
            user.is_stuff = False
            user.is_active = False
            form.save()
            username = form.cleaned_data.get("username")
            user = User.objects.get(username=username)
            get_token(request, user)
            messages.info(request, "Вам на email отправленно письмо с сылкой для авторизации!")
            return redirect('women:women_homepage')
    else:
        form = RegisterUserForm()
    return render(request, 'users/register.html', {'form': form})

