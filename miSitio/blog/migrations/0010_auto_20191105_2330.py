# Generated by Django 2.2.6 on 2019-11-06 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20191105_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen1',
            field=models.ImageField(blank=True, upload_to='media/{{author.value_to_string}}'),
        ),
    ]
