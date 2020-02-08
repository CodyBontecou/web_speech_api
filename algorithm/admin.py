from django.contrib import admin

from .models import Card, Practice


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    pass


@admin.register(Practice)
class PracticeAdmin(admin.ModelAdmin):
    pass
