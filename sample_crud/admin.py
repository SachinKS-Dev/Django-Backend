from django.contrib import admin

from .models import SampleNote


@admin.register(SampleNote)
class SampleNoteAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at")
    search_fields = ("title", "body")
