# Generated by Django 4.1.2 on 2023-10-26 19:53

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ("cards", "0007_alter_card_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="card",
            name="image",
            field=django_resized.forms.ResizedImageField(
                blank=True,
                crop=["middle", "center"],
                force_format=None,
                help_text="Icon should be at least 200x200 px. Icon will be automatically cropped otherwise.",
                keep_meta=True,
                null=True,
                quality=-1,
                scale=None,
                size=[200, 200],
                upload_to="images",
            ),
        ),
    ]