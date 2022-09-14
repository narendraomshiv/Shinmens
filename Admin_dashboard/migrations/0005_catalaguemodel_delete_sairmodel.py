# Generated by Django 4.0.4 on 2022-09-07 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_dashboard', '0004_sairmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalagueModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('year', models.CharField(blank=True, max_length=20, null=True)),
                ('heading', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='SAirModel',
        ),
    ]
