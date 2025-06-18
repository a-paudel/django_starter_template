from django.forms import BaseForm as _DjangoBaseForm
from django.forms import widgets


class BaseForm(_DjangoBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            initial_classes: str = field.widget.attrs.get("class", "")
            default_classes = ""
            error_classes = ""

            if not initial_classes.strip():
                if isinstance(field.widget, widgets.Select):
                    default_classes = "select select-bordered w-full"
                    error_classes = "select-error"
                elif isinstance(field.widget, widgets.Textarea):
                    default_classes = "textarea textarea-bordered w-full"
                    error_classes = "textarea-error"
                elif isinstance(field.widget, widgets.FileInput):
                    default_classes = "file-input w-full"
                    error_classes = "file-input-error"
                elif isinstance(field.widget, widgets.CheckboxInput):
                    default_classes = "toggle toggle-primary"
                elif isinstance(field.widget, widgets.RadioSelect):
                    default_classes = "radio radio-primary"
                else:
                    default_classes = "input input-bordered w-full"
                    error_classes = "input-error"

            initial_classes += " " + default_classes
            if field_name in self.errors:
                initial_classes += " " + error_classes

            field.widget.attrs["class"] = initial_classes.strip()
