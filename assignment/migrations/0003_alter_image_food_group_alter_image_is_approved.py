# Generated by Django 4.0.2 on 2022-03-01 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0002_image_food_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='food_group',
            field=models.CharField(choices=[(1, 'Veg'), (2, 'Fruit'), (3, 'Grain'), (4, 'Protein'), (5, 'Dairy'), (6, 'Confectionary'), (7, 'Unknown')], default='1', max_length=20, verbose_name='Food Group'),
        ),
        migrations.AlterField(
            model_name='image',
            name='is_approved',
            field=models.BooleanField(verbose_name='Is Approved'),
        ),
    ]
