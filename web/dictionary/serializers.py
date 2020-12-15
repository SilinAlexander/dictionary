from rest_framework import serializers
from .models import Word, Category, Level, Theme


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'icon')


class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = ('id', 'name', 'code')


class ShortWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('id', 'name')


class ThemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Theme
        fields = ('id', 'name', 'category', 'level', 'photo')


class ThemeRetrieveSerializer(ThemeSerializer):
    words = ShortWordSerializer(source='word_set', many=True)

    class Meta(ThemeSerializer.Meta):
        fields = ('id', 'name', 'category', 'level', 'photo', 'words')


class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Word
        fields = ('id', 'name', 'translation', 'transcription', 'example', 'sound')
