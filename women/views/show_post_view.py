from django.shortcuts import render, get_object_or_404
from women.models import Women


def show_post(request, post_slug):
    """Функция отображения одиночного поста."""
    post = get_object_or_404(Women.objects.filter(slug=post_slug))
    return render(request, 'women/women_single_post.html', {'post': post})
