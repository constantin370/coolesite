from django.shortcuts import get_list_or_404

from women.models.women_model import Women
from women.utils import paginator


def show_category(request, cat_slug):
    """Функция представления списка женщин по категориям."""
    templates = 'women/category_list.html'
    category_women = get_list_or_404(Women.objects.select_related('cat').filter(cat__slug=cat_slug))
    return paginator(request, templates, category_women)