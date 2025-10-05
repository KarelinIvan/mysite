from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse

NULLABlE = {'blank': True, 'null': True}


class PublishedManager(models.Manager):
    """ Класс для формирования отображения только статей имеющих статус опубликовано """
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class Post(models.Model):
    """ Модель статьи """

    class Status(models.TextChoices):
        """ Статус статьи """
        DRAFT = 'DF', 'Черновик'
        PUBLISHED = 'PB', 'Опубликовано'

    title = models.CharField(max_length=250, verbose_name='Наименование')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts',
                               verbose_name='Автор статьи')
    image = models.ImageField(verbose_name='Изображение', **NULLABlE)
    content = models.TextField(verbose_name='Контент')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT, verbose_name='Статус')
    objects = models.Manager() #Применяется по умолчанию
    published = PublishedManager()
    slug = models.SlugField(max_length=250, unique_for_date='publish', verbose_name='Короткая метка')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if not self.publish:
            self.publish = timezone.now()
            self.save()
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish']), ]
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
