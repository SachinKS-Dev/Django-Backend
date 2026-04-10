from rest_framework import serializers

from .models import SampleNote


class SampleNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleNote
        fields = ["id", "title", "body", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
