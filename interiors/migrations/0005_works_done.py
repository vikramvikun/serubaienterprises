# Generated by Django 3.0.6 on 2020-07-28 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interiors', '0004_subservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='works_done',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='media')),
            ],
        ),
    ]
