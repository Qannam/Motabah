# Generated by Django 3.0.3 on 2020-02-24 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eval', '0005_criteria_arabic_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criteria',
            name='arabic_name',
            field=models.TextField(max_length=1001),
        ),
    ]
