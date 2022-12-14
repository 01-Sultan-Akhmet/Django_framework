# Generated by Django 4.0.2 on 2022-03-23 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Game name')),
                ('type', models.CharField(max_length=50, verbose_name='Game type')),
                ('popularity', models.CharField(max_length=50, verbose_name='Game popularity')),
                ('buy', models.CharField(max_length=50, verbose_name='Buy game')),
                ('date', models.DateTimeField(verbose_name='Today:')),
            ],
        ),
    ]
