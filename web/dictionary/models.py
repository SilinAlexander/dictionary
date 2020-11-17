from django.db import models

# Create your models here.
skill_level = (
    (0, 'pre-intermediate'),
    (1, 'intermediate'),
    (2, 'upper-intermediate')
)
DEFAULT = 'icon/default.jpg'


def icon_upload_path(self, filename):
    """file will be uploaded to MEDIA_ROOT / icon  / category_id / <filename>"""
    return f"profiles/{getattr(self, 'category_id')}/{filename}"


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def _str_(self):
        return self.title


# class Word(models.Model):
#     title = models.CharField(max_length=120)
#     category = models.TextField()
#     level = models.TextField()
#     theme = models.TextField()
#     stw = models.TextField()
#     example = models.TextField()
#     transcription = models.TextField()
#     user = models.ForeignKey('User', related_name='words', on_delete=models.CASCADE)
#
#     def _str_(self):
#         return self.title
class Word(models.Model):
    word = models.CharField(max_length=60)


class Category(models.Model):
    name = models.CharField(max_length=120)
    icon = models.ImageField(upload_to=icon_upload_path, default=DEFAULT)


class Level(models.Model):
    level = models.CharField(choices=skill_level, default=skill_level[0])


class Theme(models.Model):
    name = models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='theme_set')
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True)
    word = models.ManyToManyField(Word, related_name='word_set', )






