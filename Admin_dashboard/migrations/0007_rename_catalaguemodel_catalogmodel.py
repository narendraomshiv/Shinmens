# Generated by Django 4.1 on 2022-09-08 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Admin_dashboard", "0006_catalaguemodel_delete_sairmodel"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="CatalagueModel",
            new_name="CatalogModel",
        ),
    ]