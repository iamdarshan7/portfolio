# Generated by Django 3.1.3 on 2020-11-30 05:12

from django.db import migrations, models
import mysite.validators


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20201128_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='phone',
            field=models.CharField(default=2020, max_length=10, validators=[mysite.validators.validate_number]),
            preserve_default=False,
        ),
    ]