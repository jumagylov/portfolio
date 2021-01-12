from django.db import models
from django.urls import reverse
from django.utils import timezone


class Portfolio(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    img = models.ImageField(null=True, blank=True, upload_to='portfolio/static/images/portfolio',
                            verbose_name='Изображение')
    description = models.TextField(max_length=200, verbose_name='Описание')

    def __str__(self):
        return self.title


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(null=True, blank=True, upload_to='portfolio/static/images/blog/', verbose_name='images')
    objects = models.Manager()

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def str(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio:post_detail', args=[self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

        def __str__(self):
            return 'Comment by {} on {}'.format(self.name, self.post)


