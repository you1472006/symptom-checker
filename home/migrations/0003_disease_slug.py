# Generated by Django 4.2.4 on 2023-08-10 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_sym_disease_symptoms'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='slug',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
