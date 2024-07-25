import uuid
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse_lazy


def get_token(request, user):
    """Функция создания токена и кодировки пользователя."""
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    current_site = get_current_site(request)
    activation_url = reverse_lazy('users:verifyemail', kwargs={'uidb64': uid, 'token': uuid.uuid4().hex})
    message = (f'http://{current_site.domain}{activation_url}')
    email = EmailMessage('Confirm your email address by clicking on the following link',
                         message,
                         to=[user.email])
    email.send()


