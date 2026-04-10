from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .defaults import deep_merge_dict
from .models import StoreTheme
from .service import build_theme_payload


@method_decorator(ensure_csrf_cookie, name="dispatch")
class ThemeView(APIView):
    authentication_classes = [SessionAuthentication]

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAdminUser()]

    def get(self, request):
        return Response(build_theme_payload(request))

    def patch(self, request):
        row = StoreTheme.get_solo()
        body = request.data if isinstance(request.data, dict) else {}
        current = row.tokens or {}
        if "colors" in body and isinstance(body["colors"], dict):
            current["colors"] = deep_merge_dict(
                current.get("colors") or {},
                body["colors"],
            )
        if "text" in body and isinstance(body["text"], dict):
            current["text"] = deep_merge_dict(
                current.get("text") or {},
                body["text"],
            )
        if "assets" in body and isinstance(body["assets"], dict):
            current["assets"] = deep_merge_dict(
                current.get("assets") or {},
                body["assets"],
            )
        row.tokens = current
        row.save(update_fields=["tokens", "updated_at"])
        return Response(build_theme_payload(request))
