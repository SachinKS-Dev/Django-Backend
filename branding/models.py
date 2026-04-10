from django.db import models


class StoreTheme(models.Model):
    """
    Per-deployment storefront branding (singleton pattern: use .get_solo()).
    Partial JSON in `tokens` merges over branding.defaults.DEFAULT_THEME.
    """

    store_name = models.CharField(max_length=200, blank=True, default="")
    tagline = models.CharField(max_length=300, blank=True, default="")
    footer_legal = models.TextField(blank=True, default="")
    support_email = models.EmailField(blank=True, default="")
    seo_title = models.CharField(max_length=200, blank=True, default="")
    seo_description = models.TextField(blank=True, default="")
    logo = models.ImageField(upload_to="branding/", blank=True, null=True)
    logo_compact = models.ImageField(upload_to="branding/", blank=True, null=True)
    favicon = models.ImageField(upload_to="branding/", blank=True, null=True)
    og_image = models.ImageField(upload_to="branding/", blank=True, null=True)
    tokens = models.JSONField(default=dict, blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Store theme"
        verbose_name_plural = "Store theme"

    def __str__(self) -> str:
        return self.store_name or "Store theme"

    @classmethod
    def get_solo(cls) -> "StoreTheme":
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj
