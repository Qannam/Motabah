# Generated by Django 3.0.3 on 2020-02-24 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_customuser_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='arabic_name',
            field=models.CharField(default='no name', max_length=200),
            preserve_default=False,
        ),
    ]