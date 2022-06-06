# Generated by Django 3.2.8 on 2021-10-13 05:42

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gjs_app', '0003_alter_post_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='work_from',
            field=models.CharField(choices=[('WORK FROM HOME', 'Work From Home')], default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='hiring_process',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('FACE TO FACE', 'Face to Face'), ('WRITTEN', 'Written'), ('TELEPHONIC', 'Telephonic'), ('GROUP DISCUSSION', 'Group Discussion'), ('WALK-IN', 'Walk-In')], max_length=56),
        ),
    ]