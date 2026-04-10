import json
from pathlib import Path

from django.conf import settings
from django.http import HttpRequest

from .defaults import DEFAULT_THEME, deep_merge_dict
from .models import StoreTheme


def _local_theme_file_overlay() -> dict:
    path = Path(settings.BASE_DIR) / "theme.local.json"
    if not path.is_file():
        return {}
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


def build_theme_payload(request: HttpRequest | None) -> dict:
    row = StoreTheme.objects.filter(pk=1).first()
    tok = (row.tokens if row else None) or {}
    file_overlay = _local_theme_file_overlay()

    merged_colors = deep_merge_dict(
        dict(DEFAULT_THEME["colors"]),
        file_overlay.get("colors") or {},
    )
    merged_colors = deep_merge_dict(merged_colors, tok.get("colors") or {})

    merged_text = deep_merge_dict(
        dict(DEFAULT_THEME["text"]),
        file_overlay.get("text") or {},
    )
    merged_text = deep_merge_dict(merged_text, tok.get("text") or {})

    merged_assets = deep_merge_dict(
        dict(DEFAULT_THEME["assets"]),
        file_overlay.get("assets") or {},
    )
    merged_assets = deep_merge_dict(merged_assets, tok.get("assets") or {})

    if row:
        if row.store_name:
            merged_text["storeName"] = row.store_name
        if row.tagline:
            merged_text["tagline"] = row.tagline
        if row.footer_legal:
            merged_text["footerLegal"] = row.footer_legal
        if row.support_email:
            merged_text["supportEmail"] = row.support_email
        if row.seo_title:
            merged_text["defaultTitle"] = row.seo_title
        if row.seo_description:
            merged_text["defaultDescription"] = row.seo_description

        def media_url(f) -> str | None:
            if not f or not getattr(f, "name", None):
                return None
            if request:
                return request.build_absolute_uri(f.url)
            return f.url

        if row.logo:
            merged_assets["logoUrl"] = media_url(row.logo)
        if row.logo_compact:
            merged_assets["logoCompactUrl"] = media_url(row.logo_compact)
        if row.favicon:
            merged_assets["faviconUrl"] = media_url(row.favicon)
        if row.og_image:
            merged_assets["ogImageUrl"] = media_url(row.og_image)

    return {
        "themeVersion": DEFAULT_THEME["themeVersion"],
        "colors": merged_colors,
        "text": merged_text,
        "assets": merged_assets,
    }
