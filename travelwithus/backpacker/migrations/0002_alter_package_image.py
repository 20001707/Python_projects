# Generated by Django 4.0 on 2022-02-22 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backpacker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='image',
            field=models.ImageField(default='', null=True, upload_to=''),
        ),
    ]
