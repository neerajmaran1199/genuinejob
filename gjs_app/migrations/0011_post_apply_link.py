# Generated by Django 3.2.8 on 2021-10-16 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gjs_app', '0010_alter_post_work_from'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='apply_link',
            field=models.URLField(default=0),
            preserve_default=False,
        ),
    ]