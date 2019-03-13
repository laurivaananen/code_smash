from django.db import models
from django.contrib.auth.models import User

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    content_panels = Page.content_panels

    max_count = 1

    class Meta:
        verbose_name = "Homepage"


class BlogPage(Page):
    header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    intro = models.CharField("Blog intro", null=True, blank=True, max_length=2048)
    body = StreamField([
        ('heading', blocks.CharBlock(template='blog/blocks/heading.html')),
        ('paragraph', blocks.RichTextBlock(features=['bold', 'italic', 'link'])),
        ('image', ImageChooserBlock(template='blog/blocks/image.html')),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('header_image'),
        FieldPanel('intro'),
        StreamFieldPanel('body'),
    ]

    parent_page_types = ['blog.HomePage']
    subpage_types = []

    class Meta:
        verbose_name = "Blogpage"