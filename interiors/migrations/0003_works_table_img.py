# Generated by Django 3.0.6 on 2020-07-27 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interiors', '0002_auto_20200727_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='works_table',
            name='img',
            field=models.ImageField(default=0, upload_to='media'),
            preserve_default=False,
        ),
    ]