# Generated by Django 2.1.7 on 2019-03-24 14:35

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190320_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(template='blog/blocks/heading.html')), ('paragraph', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'])), ('image', wagtail.images.blocks.ImageChooserBlock(template='blog/blocks/image.html')), ('code', wagtail.core.blocks.StructBlock([('code', wagtail.core.blocks.TextBlock()), ('lang', wagtail.core.blocks.ChoiceBlock(choices=[('html', 'html'), ('python', 'python')]))]))], blank=True, null=True),
        ),
    ]
