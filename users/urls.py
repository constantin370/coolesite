from django.urls import path

from users.views.register_user_view import register_user_view
from users.views.user_confirm_email import get_verify_email


app_name = "users"


urlpatterns = [
    path('register/', register_user_view, name='register'),
    path('verify-email/<str:uidb64>/<str:token>/', get_verify_email, name='verifyemail'),

]