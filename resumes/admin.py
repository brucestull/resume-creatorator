from django.contrib import admin

from .models import ProfessionalName


@admin.register(ProfessionalName)
class ProfessionalNameAdmin(admin.ModelAdmin):
    list_display = ["user", "first", "middle", "last", "suffix"]
    search_fields = [
        "user__username",
        "user__email",
        "first",
        "middle",
        "last",
        "suffix",
    ]
    list_filter = ["created", "updated"]
    readonly_fields = ["created", "updated"]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "user",
                    "first",
                    "middle",
                    "last",
                    "suffix",
                )
            },
        ),
        (
            "Important Dates",
            {
                "fields": (
                    "created",
                    "updated",
                ),
                "classes": ("collapse",),
            },
        ),
    )
