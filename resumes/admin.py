from django.contrib import admin

from .models import ProfessionalName, TechnicalSkillType, TechnicalSkill


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


@admin.register(TechnicalSkillType)
class TechnicalSkillTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["created", "updated"]
    readonly_fields = ["created", "updated"]
    fieldsets = (
        (
            None,
            {"fields": ("name",)},
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


@admin.register(TechnicalSkill)
class TechnicalSkillAdmin(admin.ModelAdmin):
    list_display = ["name", "skill_type", "user", "order"]
    search_fields = [
        "user__username",
        "user__email",
        "skill_type__name",
        "name",
    ]
    list_filter = ["created", "updated"]
    readonly_fields = ["created", "updated"]
    fieldsets = (
        (
            None,
            {"fields": ("user", "skill_type", "name")},
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
