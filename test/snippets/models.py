from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet


@register_snippet
class ContentCategory(models.Model):
    title = models.TextField(verbose_name="Title", blank=True)

    panels = [
        FieldPanel("title"),
    ]

    def __str__(self):
        if self.title:
            return self.title
        return super().__str__()

    preview_modes = []

    class Meta:
        verbose_name = "Content category"


@register_snippet
class NewsCategory(models.Model):

    preview_modes = []

    class Meta:
        verbose_name = "News category"
