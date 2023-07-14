# Generated by Django 4.0.1 on 2023-07-04 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0064_blog_reviewed_by_blog_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('from_user', models.IntegerField()),
                ('to_user', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('redirect_location', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('read_receipt', models.BooleanField(default=False)),
            ],
        ),
    ]