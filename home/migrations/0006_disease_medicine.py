# Generated by Django 4.2.4 on 2023-08-10 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_disease_slug_symptom_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='medicine',
            field=models.TextField(default=' '),
        ),
    ]
