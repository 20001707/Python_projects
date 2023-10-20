# Generated by Django 4.0 on 2022-02-26 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backpacker', '0005_alter_package_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='mode',
            field=models.CharField(choices=[('T', 'Train'), ('B', 'Bus'), ('F', 'Flight')], default='B', max_length=1),
        ),
        migrations.AlterField(
            model_name='package',
            name='slots',
            field=models.IntegerField(default=2),
        ),
    ]
