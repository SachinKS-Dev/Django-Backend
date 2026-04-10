"""Canonical default theme — keep keys aligned with React `defaultTheme.ts`."""

DEFAULT_THEME = {
    "themeVersion": 1,
    "colors": {
        "primary": "#1a1a1a",
        "primaryForeground": "#ffffff",
        "secondary": "#f4f4f5",
        "secondaryForeground": "#18181b",
        "accent": "#3b82f6",
        "accentForeground": "#ffffff",
        "background": "#f6f6f6",
        "surface": "#ffffff",
        "muted": "#f4f4f5",
        "mutedForeground": "#71717a",
        "border": "#e4e4e7",
        "destructive": "#dc2626",
        "destructiveForeground": "#ffffff",
        "success": "#16a34a",
        "successForeground": "#ffffff",
    },
    "text": {
        "storeName": "Storefront",
        "tagline": "Your e-commerce platform",
        "footerLegal": "",
        "supportEmail": "",
        "defaultTitle": "Storefront",
        "defaultDescription": "Shop powered by FullStack",
    },
    "assets": {
        "logoUrl": None,
        "logoCompactUrl": None,
        "faviconUrl": None,
        "ogImageUrl": None,
    },
}


def deep_merge_dict(base: dict, overlay: dict | None) -> dict:
    if not overlay:
        return dict(base)
    out = dict(base)
    for k, v in overlay.items():
        if k in out and isinstance(out[k], dict) and isinstance(v, dict):
            out[k] = deep_merge_dict(out[k], v)
        elif v is not None:
            out[k] = v
    return out
