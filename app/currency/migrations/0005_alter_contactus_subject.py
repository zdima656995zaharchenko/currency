# Generated by Django 4.2.3 on 2023-07-27 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0004_alter_contactus_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='subject',
            field=models.CharField(max_length=100),
        ),
    ]
