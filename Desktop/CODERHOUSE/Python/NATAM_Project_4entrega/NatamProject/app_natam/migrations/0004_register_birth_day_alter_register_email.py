# Generated by Django 5.1.1 on 2024-09-21 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_natam', '0003_remove_register_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='birth_day',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
