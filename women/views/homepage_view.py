from django.shortcuts import render


def homepage(request):
    """Функция отображения домашней страницы."""
    return render(request, 'women/homepage.html')