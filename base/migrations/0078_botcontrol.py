# Generated by Django 4.0.1 on 2023-07-10 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0077_alter_student_mail_id_alter_student_parent_mail_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='BotControl',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('usr_id', models.IntegerField(unique=True)),
                ('toggle', models.IntegerField(blank=True)),
            ],
        ),
    ]