# Generated by Django 3.2.8 on 2021-10-15 03:53

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gjs_app', '0007_alter_post_work_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='work_from',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('WORK FROM HOME', 'Work From Home')], max_length=14, null=True),
        ),
    ]
