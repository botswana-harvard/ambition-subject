# Generated by Django 2.0.1 on 2018-01-21 12:56

from django.db import migrations, models
import django.utils.timezone
import edc_base.model_validators.date


class Migration(migrations.Migration):

    dependencies = [
        ('ambition_subject', '0002_auto_20180119_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicallumbarpuncturecsf',
            name='lp_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, validators=[edc_base.model_validators.date.datetime_not_future], verbose_name='LP Date and Time'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lumbarpuncturecsf',
            name='lp_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, validators=[edc_base.model_validators.date.datetime_not_future], verbose_name='LP Date and Time'),
            preserve_default=False,
        ),
    ]
