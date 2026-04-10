from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import SampleNote
from .serializers import SampleNoteSerializer


class SampleNoteViewSet(ModelViewSet):
    """
    Demo-only CRUD API. Uses AllowAny for local learning; replace with real
    authentication for production.
    """

    serializer_class = SampleNoteSerializer
    authentication_classes = []
    permission_classes = [AllowAny]

    def get_queryset(self):
        return SampleNote.objects.all().order_by("-created_at")
