from django.shortcuts import get_list_or_404
from django.http import HttpResponse
from women.models.women_model import Women
from women.utils import paginator


def search(request):
    """Функция поиска по имени известных женщин."""
    templates = 'women/women_list.html'
    if request.user.is_superuser or request.user.is_staff:
        queryset = get_list_or_404(Women.objects.filter(
            title__icontains=request.GET['name_input_field']))
        return paginator(request, templates, queryset)
    else:
        queryset = get_list_or_404(Women.objects.filter(
            title__icontains=request.GET['name_input_field'],
            is_published=True,
            cat__is_published=True))
        return paginator(request, templates, queryset)

