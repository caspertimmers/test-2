from test import blocks as test_blocks
from test.pages import blocks as pages_blocks

from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.search import index
from wagtail.snippets import edit_handlers as snippet_edit_handlers


class NewsOverviewPage(Page):

    subpage_types = [
        "pages.NewsPage",
        "pages.HoebaTypePage",
    ]
    parent_page_types = [
        "pages.HoebaTypePage",
        "pages.HomePage",
    ]

    preview_modes = []

    class Meta:
        verbose_name = "News overview page"


class HomePage(Page):
    header = models.TextField(verbose_name="Header", blank=True)
    content = StreamField(
        block_types=[
            ("paragraph", test_blocks.ParagraphBlock()),
            ("image", test_blocks.ImageBlock()),
            ("quote", test_blocks.QuoteBlock()),
        ],
        verbose_name="Content",
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("header"),
        StreamFieldPanel("content"),
    ]

    subpage_types = [
        "pages.OverviewPage",
        "pages.ContentPage",
        "pages.HoebaTypePage",
        "pages.NewsOverviewPage",
    ]
    parent_page_types = [
        "wagtailcore.Page",
        "pages.HoebaTypePage",
    ]

    preview_modes = []

    class Meta:
        verbose_name = "Homepage"


class OverviewPage(Page):
    header = models.TextField(verbose_name="Header", blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("header"),
    ]

    subpage_types = [
        "pages.ContentPage",
        "pages.HoebaTypePage",
    ]
    parent_page_types = [
        "pages.HoebaTypePage",
        "pages.HomePage",
    ]

    preview_modes = []

    class Meta:
        verbose_name = "Overview page"


class ContentPage(Page):
    category = models.ForeignKey(
        to="snippets.ContentCategory",
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Category",
        blank=True,
        null=True,
    )
    content = StreamField(
        block_types=[
            ("paragraph", test_blocks.ParagraphBlock()),
            ("image", test_blocks.ImageBlock()),
            ("quote", test_blocks.QuoteBlock()),
        ],
        verbose_name="Content",
        blank=True,
    )
    related_pages = StreamField(
        block_types=[("relatedpage", pages_blocks.RelatedPageBlock())],
        verbose_name="Related pages",
        blank=True,
    )
    header = models.TextField(verbose_name="Header", blank=True)
    downloads = StreamField(
        block_types=[("download", pages_blocks.DownloadBlock())],
        verbose_name="Downloads",
        blank=True,
    )

    content_panels = Page.content_panels + [
        snippet_edit_handlers.SnippetChooserPanel("category"),
        FieldPanel("header"),
        StreamFieldPanel("content"),
        StreamFieldPanel("related_pages"),
        StreamFieldPanel("downloads"),
    ]

    subpage_types = [
        "pages.ContentPage",
        "pages.HoebaTypePage",
    ]
    parent_page_types = [
        "pages.OverviewPage",
        "pages.ContentPage",
        "pages.HoebaTypePage",
        "pages.HomePage",
    ]

    preview_modes = []

    class Meta:
        verbose_name = "Content page"


class NewsPage(Page):
    category = models.ForeignKey(
        to="snippets.NewsCategory",
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Category",
        blank=True,
        null=True,
    )
    content = StreamField(
        block_types=[
            ("paragraph", test_blocks.ParagraphBlock()),
            ("image", test_blocks.ImageBlock()),
            ("quote", test_blocks.QuoteBlock()),
        ],
        verbose_name="Content",
        blank=True,
    )

    content_panels = Page.content_panels + [
        snippet_edit_handlers.SnippetChooserPanel("category"),
        StreamFieldPanel("content"),
    ]

    subpage_types = [
        "pages.HoebaTypePage",
    ]
    parent_page_types = [
        "pages.HoebaTypePage",
        "pages.NewsOverviewPage",
    ]

    preview_modes = []

    class Meta:
        verbose_name = "News page"


class HoebaTypePage(Page):
    kek = models.TextField(verbose_name="Kek", blank=True)
    jojo = RichTextField(verbose_name="Jojo", blank=True)
    streaamit = StreamField(
        block_types=[("daaate", pages_blocks.DaaateBlock())],
        verbose_name="Streaamit",
        blank=True,
    )

    kekjo_panels = [
        FieldPanel("kek"),
        FieldPanel("jojo"),
    ]
    content_panels = Page.content_panels + [
        MultiFieldPanel(heading="Kekjo", children=kekjo_panels),
        StreamFieldPanel("streaamit"),
    ]

    parent_page_types = [
        "pages.OverviewPage",
        "pages.ContentPage",
        "pages.NewsPage",
        "pages.HoebaTypePage",
        "pages.NewsOverviewPage",
        "pages.HomePage",
    ]

    preview_modes = []

    class Meta:
        verbose_name = "HoebaType"
