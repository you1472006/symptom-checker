# Generated by Django 4.2.4 on 2023-08-11 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_disease_medicine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symptom',
            name='description',
            field=models.TextField(default='abc'),
        ),
    ]
