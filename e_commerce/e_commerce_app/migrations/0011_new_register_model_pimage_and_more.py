# Generated by Django 4.2 on 2023-09-28 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce_app', '0010_rename_cart_cartmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='new_register_model',
            name='pimage',
            field=models.FileField(default=1, upload_to='e_commerce_app/static/images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_register_model',
            name='proimage',
            field=models.FileField(default=1, upload_to='e_commerce_app/static/images'),
            preserve_default=False,
        ),
    ]
