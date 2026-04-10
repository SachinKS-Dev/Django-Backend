from django.db import models


class SampleNote(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Sample note"
        verbose_name_plural = "Sample notes"

    def __str__(self) -> str:
        return self.title
