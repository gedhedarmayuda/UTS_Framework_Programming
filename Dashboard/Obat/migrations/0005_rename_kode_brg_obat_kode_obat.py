# Generated by Django 4.1.2 on 2022-11-17 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Obat', '0004_obat_supplier'),
    ]

    operations = [
        migrations.RenameField(
            model_name='obat',
            old_name='kode_brg',
            new_name='kode_obat',
        ),
    ]