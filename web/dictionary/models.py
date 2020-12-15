from django.db import models

DEFAULT_ICON = 'icon/default.jpg'
DEFAULT_THEME = 'theme/default.jpg'
DEFAULT_SOUND = ''


def upload_icon_path(self, filename):
    """file will be uploaded to MEDIA_ROOT / icon  / category_id / <filename>"""
    return f"icon/{filename}"


def upload_theme_path(self, filename):
    """file will be uploaded to MEDIA_ROOT / icon  / category_id / <filename>"""
    return f"theme/{filename}"


def upload_sound_path(self, filename):
    """file will be uploaded to MEDIA_ROOT / icon  / category_id / <filename>"""
    return f"sound/{filename}"


class Category(models.Model):
    name = models.CharField(max_length=120)
    icon = models.ImageField(upload_to=upload_icon_path, default=DEFAULT_ICON)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=120)
    code = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.name}, code {self.code}"


class Theme(models.Model):
    name = models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='theme_set')
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(upload_to=upload_theme_path, default=DEFAULT_THEME)

    def __str__(self):
        return self.name


class Word(models.Model):
    name = models.CharField(max_length=60)
    translation = models.CharField(max_length=60)
    transcription = models.CharField(max_length=60)
    example = models.TextField()
    sound = models.FileField(upload_to=upload_sound_path, default=DEFAULT_SOUND, null=True, blank=True)
    theme = models.ForeignKey(Theme, related_name='word_set', on_delete=models.CASCADE)

    def __str__(self):
        return self.name




