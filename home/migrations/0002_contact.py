# Generated by Django 4.1.2 on 2022-10-17 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('status', models.CharField(choices=[('New', 'New'), ('Pending', 'Pending'), ('Updated', 'Updated'), ('Completed', 'Completed')], default='New', max_length=50)),
                ('sent', models.DateField(auto_now=True)),
                ('updated', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
