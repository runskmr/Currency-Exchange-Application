# Generated by Django 4.0.6 on 2022-07-19 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currencyvalue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usd', models.CharField(max_length=30)),
                ('inr', models.CharField(max_length=30)),
                ('cad', models.CharField(max_length=30)),
                ('usinr', models.CharField(max_length=30)),
            ],
        ),
    ]
