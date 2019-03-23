from django.db import models
from django.contrib.auth.models import User

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel

from pygments import highlight, styles
from pygments.lexers import python, get_lexer_by_name, get_all_lexers
from pygments.formatters import html

from setuptools import setup, find_packages


class HomePage(Page):
    content_panels = Page.content_panels

    max_count = 1

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context

    class Meta:
        verbose_name = "Homepage"

class CodeBlock(blocks.StructBlock):
    code = blocks.TextBlock()
    # all_styles = [(x, x) for x in styles.get_all_styles()]
    # all_lexers = [(x[1][0], x[0]) for x in get_all_lexers()]
    # style = blocks.ChoiceBlock(choices=all_styles, default='default')
    # lexer = blocks.ChoiceBlock(choices=all_lexers, default='Python3')

    class Meta:
        template = 'blog/blocks/code_highlight.html'


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
        ('code', CodeBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('header_image'),
        FieldPanel('intro'),
        StreamFieldPanel('body'),
    ]

    parent_page_types = ['blog.HomePage']
    subpage_types = []

    def get_context(self, request):
        context = super().get_context(request)
        first_published = context['page'].first_published_at
        last_published = context['page'].last_published_at
        writer = context['page'].owner
        context['published'] = '{} by {}'.format(first_published.strftime('%d %B %Y'), writer)
        if first_published != last_published:
            context['published'] = '{}, updated {}'.format(context['published'], last_published.strftime('%d %B %Y'))
        return context

    class Meta:
        verbose_name = "Blogpage"