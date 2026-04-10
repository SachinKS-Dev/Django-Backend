from rest_framework.routers import DefaultRouter

from .views import SampleNoteViewSet

router = DefaultRouter()
router.register(r"notes", SampleNoteViewSet, basename="samplenote")

urlpatterns = router.urls
