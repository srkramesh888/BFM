# Generated by Django 3.1.1 on 2021-01-03 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ram',
            name='Photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
