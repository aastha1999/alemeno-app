# Generated by Django 4.0.2 on 2022-03-02 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0004_alter_image_food_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created On'),
        ),
    ]
