# Generated by Django 4.2.3 on 2023-09-28 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('reply_to', models.EmailField(max_length=254, verbose_name='Email')),
                ('subject', models.CharField(max_length=128, verbose_name='Subject')),
                ('body', models.CharField(max_length=1024, verbose_name='Body')),
            ],
        ),
        migrations.CreateModel(
            name='RequestResponseLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255)),
                ('request_method', models.CharField(max_length=10)),
                ('time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_url', models.CharField(max_length=255)),
                ('exchange_address', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('code_name', models.CharField(max_length=32, verbose_name='Code_name')),
            ],
            options={
                'verbose_name': 'Source',
                'verbose_name_plural': 'Sources',
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sell', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('currency', models.IntegerField(choices=[(1, 'USD'), (2, 'EUR')])),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='currency.source')),
            ],
            options={
                'verbose_name': 'Rate',
                'verbose_name_plural': 'Rates',
            },
        ),
    ]
