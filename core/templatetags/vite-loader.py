import json
from django import template
from django.utils.html import format_html
from building_manager_app import settings

register = template.Library()


@register.simple_tag
def vite_loader(name: str) -> str:
    # 🟢 DEV MODE
    if settings.DEBUG:
        return format_html(
            "<script type='module' src='http://127.0.0.1:5173/src/entry/{}.ts'></script>",
            name,
        )

    # 🔴 PROD MODE
    manifest_path = settings.BASE_DIR / "static" / "dist" / ".vite" / "manifest.json"

    with open(manifest_path, "rb+") as f:
        manifest = json.load(f)

    key = f"src/entry/{name}.ts"
    entry = manifest.get(key)

    if not entry:
        raise Exception(f"Vite entry not found in manifest: {key}")

    return format_html(
        "<script type='module' src='{}'></script>",
        settings.STATIC_URL + "dist/" + entry["file"],
    )
