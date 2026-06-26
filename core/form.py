from typing import Any

from django import forms


class BaseForm(forms.Form):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field.widget.is_hidden:
                continue

            if isinstance(field.widget, forms.CheckboxInput):
                self._add_widget_class(field_name, "form-check-input")
            elif isinstance(field.widget, forms.Select):
                self._add_widget_class(field_name, "form-select")
            else:
                self._add_widget_class(field_name, "form-control")

    def is_valid(self) -> bool:
        is_form_valid = super().is_valid()

        for field_name in self.errors:
            if field_name == "__all__":
                continue

            self._add_widget_class(field_name, "is-invalid")
            self.fields[field_name].widget.attrs["aria-describedby"] = f"{field_name}-error"

        return is_form_valid

    def _add_widget_class(self, field_name: str, class_name: str) -> None:
        widget = self.fields[field_name].widget

        current_classes = widget.attrs.get("class", "")
        classes = current_classes.split()

        if class_name not in classes:
            classes.append(class_name)
        widget.attrs["class"] = " ".join(classes)

    def add_field_error(self, field: str, error: str | list[str]) -> None:
        self.add_error(field, error)
        self._add_widget_class(field, "is-invalid")
        self.fields[field].widget.attrs["aria-describedby"] = f"{field}-error"