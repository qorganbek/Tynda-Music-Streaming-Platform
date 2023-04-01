import uuid
from django.db import models
from pydub import AudioSegment
from django.utils.translation import gettext_lazy as _


class AudioField(models.FileField):
    def __init__(self, *args, **kwargs):
        super(AudioField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if isinstance(value, AudioSegment):
            return value
        elif value is None:
            return value

        return AudioSegment.from_file(value.path)

    def get_db_prep_value(self, value, connection, prepared=False):
        if isinstance(value, AudioSegment):
            return value.export(format='wav')
        else:
            return super(AudioField, self).get_db_prep_value(value, connection, prepared=prepared)


class Audio(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    artist = models.CharField(max_length=25, blank=True, null=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    audio = models.FileField(upload_to='audio/')
    is_top = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ' ' + str(self.id)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _('Audio')
        verbose_name_plural = _('Audios')
