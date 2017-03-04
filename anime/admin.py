from django.contrib import admin

from .models import Anime, Character, Story

# Register your models here.
class StoryInline(admin.StackedInline):
    model = Story
    extra = 3

class CharacterInline(admin.StackedInline):
    model = Character
    extra = 3

class AnimeAdmin(admin.ModelAdmin):
    field = ['title', 'bc_year', 'synopsis']
    inlines = [StoryInline, CharacterInline]

admin.site.register(Anime, AnimeAdmin)
