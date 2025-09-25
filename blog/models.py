from django.db import models
from django.utils import timezone
from django.conf import settings

NULLABlE = {'blank': True, 'null': True}


class Post(models.Model):
    # Модель статьи

    class Status(models.TextChoices):
        # Статус статьи
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Publised'

    title = models.CharField(max_length=250, verbose_name='Наименование')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts',
                               verbose_name='Автор статьи')
    image = models.ImageField(verbose_name='Изображение', **NULLABlE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT, verbose_name='Статус')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish']), ]
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
