# Generated by Django 3.1.6 on 2021-05-01 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0003_auto_20210501_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='mail_attachements',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mail',
            name='mail_body',
            field=models.TextField(default='--empty--'),
        ),
    ]
