import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts import models as UserModel


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
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, blank=True, null=True)

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
    artist = models.ForeignKey(to=Artist, related_name='song', on_delete=models.CASCADE)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='song',
                                 verbose_name=_('Categories'), blank=True, null=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name=_('Image'), blank=True, null=True)
    audio = models.FileField(upload_to='audios/%Y/%m/%d/', verbose_name=_('Audio File'), blank=True, null=True)
    is_top = models.BooleanField(verbose_name=_('Is Top ?'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} {self.id}'

    class Meta:
        ordering = ['is_top', '-created_at']
        verbose_name = _('Song')
        verbose_name_plural = _('Songs')


class Favorite(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.OneToOneField(to=UserModel.CustomUser, on_delete=models.PROTECT, related_name='favorite_list')
    song = models.ManyToManyField(to=Song, related_name='song')

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f'{self.user.email}\'s Favorite Songs'


class Playlist(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=50)
    user = models.ForeignKey(to=UserModel.CustomUser, on_delete=models.PROTECT, related_name='play_list')
    song = models.ManyToManyField(to=Song, related_name='song_playlist')
    category = models.ForeignKey(to=Category, related_name='playlist_category', on_delete=models.CASCADE, blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name=_('Image'), blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class MyLibrary(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.OneToOneField(to=get_user_model(), on_delete=models.CASCADE, related_name='library')
    playlist = models.ManyToManyField(to=Playlist, related_name='my_library')

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f'{self.user} libraries'
