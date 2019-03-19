# Generated by Django 2.1.7 on 2019-03-19 21:09

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190319_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(template='blog/blocks/heading.html')), ('paragraph', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'])), ('image', wagtail.images.blocks.ImageChooserBlock(template='blog/blocks/image.html')), ('code', wagtail.core.blocks.StructBlock([('code', wagtail.core.blocks.TextBlock()), ('style', wagtail.core.blocks.ChoiceBlock(choices=['default', 'emacs', 'friendly', 'colorful', 'autumn', 'murphy', 'manni', 'monokai', 'perldoc', 'pastie', 'borland', 'trac', 'native', 'fruity', 'bw', 'vim', 'vs', 'tango', 'rrt', 'xcode', 'igor', 'paraiso-light', 'paraiso-dark', 'lovelace', 'algol', 'algol_nu', 'arduino', 'rainbow_dash', 'abap']))]))], blank=True, null=True),
        ),
    ]
