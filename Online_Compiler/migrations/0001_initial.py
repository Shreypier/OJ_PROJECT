# Generated by Django 5.0.6 on 2024-05-27 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=50)),
                ('input_data', models.TextField(blank=True, null=True)),
                ('output_data', models.TextField(blank=True, null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
