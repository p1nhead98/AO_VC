# Generated by Django 2.2.6 on 2019-11-06 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20191106_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='gameForWindows',
            field=models.FileField(blank=True, null=True, upload_to='games/'),
        ),
    ]
