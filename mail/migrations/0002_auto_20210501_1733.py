# Generated by Django 3.1.6 on 2021-05-01 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='mail_attachements',
            field=models.TextField(),
        ),
    ]
