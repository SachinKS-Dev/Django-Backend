from django.contrib import admin

from .models import SampleNote


@admin.register(SampleNote)
class SampleNoteAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at")
    list_filter = ("created_at",)
    search_fields = ("title", "body")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (None, {"fields": ("title", "body")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )
