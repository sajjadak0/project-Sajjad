import json
from django import template
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.html import format_html, format_html_join

register = template.Library()

VITE_DEV_SERVER_URL = "http://127.0.0.1:5173"


def get_entry_path(name: str) -> str:
    return f"src/entry/{name}.ts"


@register.simple_tag
def vite_loader(name: str) -> str:
    entry_path = get_entry_path(name)

    if settings.DEBUG:
        return format_html(
            '<script type="module" src="{}/{}"></script>',
            VITE_DEV_SERVER_URL,
            entry_path,
        )

    manifest_path = settings.BASE_DIR / "static" / "dist" / ".vite" / "manifest.json"

    with open(manifest_path, "rb+") as f:
        manifest = json.load(f)

    entry = manifest.get(entry_path)

    if not entry:
        raise ImproperlyConfigured(
            f"Vite entry not found in manifest: {entry_path}"
        )

    static_dist_url = f"{settings.STATIC_URL}dist/"

    css_tags = format_html_join(
        "\n",
        '<link rel="stylesheet" href="{}{}">',
        (
            (static_dist_url, css_file)
            for css_file in entry.get("css", [])
        ),
    )

    js_tag = format_html(
        '<script type="module" src="{}{}"></script>',
        static_dist_url,
        entry["file"],
    )

    return format_html(
        "{}\n{}",
        css_tags,
        js_tag,
    )   