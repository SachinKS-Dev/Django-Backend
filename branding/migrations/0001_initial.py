# Generated manually for StoreTheme (run makemigrations locally to regenerate if needed)

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StoreTheme",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("store_name", models.CharField(blank=True, default="", max_length=200)),
                ("tagline", models.CharField(blank=True, default="", max_length=300)),
                ("footer_legal", models.TextField(blank=True, default="")),
                ("support_email", models.EmailField(blank=True, default="", max_length=254)),
                ("seo_title", models.CharField(blank=True, default="", max_length=200)),
                ("seo_description", models.TextField(blank=True, default="")),
                (
                    "logo",
                    models.ImageField(blank=True, null=True, upload_to="branding/"),
                ),
                (
                    "logo_compact",
                    models.ImageField(blank=True, null=True, upload_to="branding/"),
                ),
                (
                    "favicon",
                    models.ImageField(blank=True, null=True, upload_to="branding/"),
                ),
                (
                    "og_image",
                    models.ImageField(blank=True, null=True, upload_to="branding/"),
                ),
                ("tokens", models.JSONField(blank=True, default=dict)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Store theme",
                "verbose_name_plural": "Store theme",
            },
        ),
    ]
