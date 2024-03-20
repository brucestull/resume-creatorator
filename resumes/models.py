from django.db import models

from config.settings import AUTH_USER_MODEL
from base.models import CreatedUpdatedBase


class ProfessionalName(CreatedUpdatedBase):
    """
    Model for a User's professional name to be used in resumes and social media.
    """

    user = models.OneToOneField(
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
