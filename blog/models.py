from django.db import models
from django.contrib.auth.models import User

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel

from pygments import highlight, styles
from pygments.lexers import python
from pygments.formatters import html


class HomePage(Page):
    content_panels = Page.content_panels

    max_count = 1

    class Meta:
        verbose_name = "Homepage"


class CodeStructValue(blocks.StructValue):
    def formatted_code(self):
        html_formatter = html.HtmlFormatter(
            cssclass='syntax-highlight',
            classprefix='pygment-',
            linenos='inline',
            noclasses=True,
            hl_lines=[9,10,11,12,13,14],
            style=self.get('style'),
        )
        print(list(styles.get_all_styles()))
        highlighted_code = highlight(
            self.get('code'),
            python.Python3Lexer(),
            html_formatter)
        return highlighted_code


class CodeBlock(blocks.StructBlock):
    code = blocks.TextBlock()
    style = blocks.ChoiceBlock(choices=[(x, x) for x in styles.get_all_styles()], default='default')

    class Meta:
        template = 'blog/blocks/code_highlight.html'
        value_class = CodeStructValue


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

    class Meta:
        verbose_name = "Blogpage"


