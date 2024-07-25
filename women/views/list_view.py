from django.shortcuts import get_list_or_404
from women.models.women_model import Women
from women.utils import paginator


def women_list_view(request):
    """Функция отображения всех опубликованных статей."""
    templates = 'women/women_list.html'
    if request.user.is_superuser or request.user.is_staff:
        posts = get_list_or_404(Women.objects.all())
        return paginator(request, templates, posts)
    else:
        posts = get_list_or_404(Women.objects.filter(is_published=True, cat__is_published=True))
        return paginator(request, templates, posts)

