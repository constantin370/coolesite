from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.utils.http import urlsafe_base64_decode


User = get_user_model()


def get_verify_email(request, uidb64, token):
    """Функция декодирования пользователя, 
    проверка токена и его аутендификации."""
    try:
        uid = urlsafe_base64_decode(uidb64)
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and token:
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, "Вы успешно авторизовались!")
        return redirect('women:women_homepage')
    else:
        messages.warning(request, "Произошла ошибка авторизации!")
        return redirect('women:women_homepage')