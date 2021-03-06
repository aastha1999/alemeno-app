# Generated by Django 4.0.2 on 2022-03-01 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Kid Name')),
                ('age', models.IntegerField(verbose_name='Kid Age')),
                ('phone', models.CharField(max_length=12, verbose_name='Parent Phone Number')),
                ('email', models.EmailField(max_length=254, verbose_name='Parent Email Address')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='Image URL')),
                ('created_on', models.DateTimeField(verbose_name='Created On')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated On')),
                ('is_approved', models.BooleanField(verbose_name='IsApproved')),
                ('approved_by', models.CharField(max_length=20, verbose_name='Approved by')),
                ('kid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.kid')),
            ],
        ),
    ]
