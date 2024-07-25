from django.http import Http404
from django.views.generic import ListView
from django.shortcuts import get_list_or_404
from women.models.women_model import Women


class Search(ListView):
    """Класс представления поиска по имени известных женщин."""

    template_name = 'women/women_list.html'
    context_object_name = 'search_women'
    paginate_by = 3

    def get_queryset(self):
        if self.request.GET['name_input_field'] != '':
            return get_list_or_404(Women.objects.filter(is_published=True,
                                        cat__is_published=True,
                                        title__icontains=self.request.GET.get('name_input_field')))
        else:
            raise Http404('<h1>Страница не найдена</h1>')
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_input_field'] = self.request.GET.get('name_input_field')
        return context