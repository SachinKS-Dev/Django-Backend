from django.contrib import admin

from .models import StoreTheme


@admin.register(StoreTheme)
class StoreThemeAdmin(admin.ModelAdmin):
    list_display = ("store_name", "updated_at")
    fieldsets = (
        (
            "Identity & SEO",
            {
                "fields": (
                    "store_name",
                    "tagline",
                    "footer_legal",
                    "support_email",
                    "seo_title",
                    "seo_description",
                )
            },
        ),
        (
            "Assets",
            {"fields": ("logo", "logo_compact", "favicon", "og_image")},
        ),
        (
            "Advanced tokens (JSON merge over defaults)",
            {
                "fields": ("tokens",),
                "description": "Optional nested keys: colors, text, assets — merged with code defaults.",
            },
        ),
    )

    def has_add_permission(self, request):
        return not StoreTheme.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
