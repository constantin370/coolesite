from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


def paginator(request, templates, posts):
    """Функция Пагинатор."""
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)  # возвращает желаемый объект страницы
    except PageNotAnInteger:
        # если page_number не является целым числом, то назначьте первую страницу
        page_obj = paginator.page(1)
    except EmptyPage:
        # если страница пуста, то верните последнюю страницу
        page_obj = paginator.page(paginator.num_pages)
    # отправка объекта страницы в women/index.html
    return render(request, templates, {'page_obj': page_obj})