import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=25, verbose_name=_('Category name'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.id}'

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Artist(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    second_name = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.username} {self.id}'

    class Meta:
        verbose_name = _('Artist')
        verbose_name_plural = _('Artists')


class Song(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=100, unique=True, verbose_name=_('Title'))
    artist = models.ManyToManyField(to=Artist, related_name='artist', verbose_name=_('Artists'))
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='category', verbose_name=_('Categories'))
    image = models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name=_('Image'))
    audio = models.FileField(upload_to='audios/%Y/%m/%d/', verbose_name=_('Audio File'))
    is_top = models.BooleanField(verbose_name=_('Is Top ?'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} {self.id}'

    class Meta:
        ordering = ['is_top', '-created_at']
        verbose_name = _('Song')
        verbose_name_plural = _('Songs')


