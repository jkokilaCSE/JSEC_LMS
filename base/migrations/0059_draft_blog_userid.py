# Generated by Django 4.0.1 on 2023-07-02 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0058_draft_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='draft_blog',
            name='userid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]