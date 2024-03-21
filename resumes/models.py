from base.mixins import OrderableMixin
from base.models import CreatedUpdatedBase
from config.settings import AUTH_USER_MODEL
from django.db import models


class ProfessionalName(CreatedUpdatedBase):
    """
    Model for a User's professional name to be used in resumes and social media.
    """

    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="professional_name",
    )
    first = models.CharField(
        "First Name",
        max_length=255,
        help_text="The user's professional first name.",
    )
    middle = models.CharField(
        "Middle Name",
        max_length=255,
        help_text="The user's professional middle name.",
        blank=True,
    )
    last = models.CharField(
        "Last Name",
        max_length=255,
        help_text="The user's professional last name.",
    )
    suffix = models.CharField(
        "Suffix",
        max_length=255,
        help_text="The user's professional suffix.",
        blank=True,
    )

    def __str__(self):
        return f"{self.first} {self.middle} {self.last}"

    class Meta:
        verbose_name = "Professional Name"
        verbose_name_plural = "Professional Names"


class TechnicalSkillType(CreatedUpdatedBase):
    """
    Model for a type of skill that can be used in a resume.
    """

    name = models.CharField(
        "Name",
        max_length=255,
        help_text="The name of the skill type.",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Skill Type"
        verbose_name_plural = "Skill Types"


class TechnicalSkill(OrderableMixin, CreatedUpdatedBase):
    """
    Model for a technical skill that can be used in a resume.
    """

    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="technical_skills",
    )
    skill_type = models.ForeignKey(
        TechnicalSkillType,
        on_delete=models.CASCADE,
        related_name="technical_skills",
    )
    name = models.CharField(
        "Name",
        max_length=255,
        help_text="The name of the technical skill.",
    )

    order = models.PositiveIntegerField(
        "Order",
        help_text="The order of the technical skill.",
        default=255,
    )

    def save(self, *args, **kwargs):
        if not self.pk and not hasattr(self, "order"):
            highest_order = TechnicalSkill.objects.all().aggregate(models.Max("order"))[
                "order__max"
            ]
            self.order = (highest_order if highest_order is not None else -1) + 1
        super(TechnicalSkill, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Technical Skill"
        verbose_name_plural = "Technical Skills"
