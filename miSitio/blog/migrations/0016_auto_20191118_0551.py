# Generated by Django 2.2.6 on 2019-11-18 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20191116_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='gameForWindows',
            field=models.FileField(upload_to='games/'),
        ),
    ]
