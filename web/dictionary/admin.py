from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from .models import Word, Theme, Category, Level


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('name', 'sound', 'sound_player')

    def sound_player(self, obj):

        if obj.sound:
            url = obj.sound.url
            return mark_safe(f"<audio controls> <source src='{ url }' type='audio/mpeg'> </audio>")
        return 'sound is absent'


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'category', 'get_photo')

    def get_photo(self, obj):
        url = obj.photo.url
        return mark_safe(f"<img src='{url}' width='50' height='50'>")

    get_photo.short_description = 'photo'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_icon')
    fields = ('name', 'icon', 'get_icon', )
    readonly_fields = ('get_icon', )

    def get_icon(self, obj):
        url = obj.icon.url
        return mark_safe(f"<img src='{url}' width='50' height='50'>")

    get_icon.short_description = 'icon'


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    pass
