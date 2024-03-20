from django.urls import path
from django.views.generic import TemplateView

from config.settings import THE_SITE_NAME


app_name = "resumes"
urlpatterns = [
    path(
        "",
        view=TemplateView.as_view(
            template_name="resumes/home.html",
            extra_context={
                "page_title": "Resume Madness!",
                "the_site_name": THE_SITE_NAME,
            },
        ),
        name="home",
    ),
]
