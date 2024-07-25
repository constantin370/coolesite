from django.db import models

from django.urls import reverse

# Create your models here.


class Women(models.Model):
    """Модель списка всех известных женщин."""
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(verbose_name='Текст', blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    time_create = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
    is_published = models.BooleanField(verbose_name='Опубликовать', default=True)
    # Список категорий, на которые Women ссылается через внешний ключ cat.
    cat = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.PROTECT)

    def __str__(self):
        """Возвращает заголовок женщины
        как ее строковое представление."""
        return self.title

    def get_absolute_url(self):
        """Метод возвращает URL страницы
        с информацией о конкретной женщине."""
        return reverse('women:women_single_post', kwargs={'post_slug': self.slug})
    
    class Meta:
        """Для понятного отображения названий."""
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины'
        ordering = ['-time_create', 'title']