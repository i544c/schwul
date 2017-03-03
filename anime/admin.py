from django.contrib import admin

from .models import Anime, Story

# Register your models here.
class StoryInline(admin.StackedInline):
    model = Story
    extra = 3

class AnimeAdmin(admin.ModelAdmin):
    field = ['title', 'bc_year', 'synopsis']
    inlines = [StoryInline]

admin.site.register(Anime, AnimeAdmin)
