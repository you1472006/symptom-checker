# Generated by Django 4.2.4 on 2023-08-11 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_symptom_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='symptom',
            name='description',
        ),
    ]