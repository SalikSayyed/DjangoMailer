# Generated by Django 3.1.6 on 2021-05-01 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0002_auto_20210501_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='mail_attachements',
            field=models.FileField(upload_to=''),
        ),
    ]
