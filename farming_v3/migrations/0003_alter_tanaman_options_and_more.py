# Generated by Django 5.0.2 on 2025-03-10 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farming_v3', '0002_alter_hama_rate_bahaya'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tanaman',
            options={'ordering': ['-harga_per_ton']},
        ),
        migrations.RenameField(
            model_name='tanaman',
            old_name='harga_perTon',
            new_name='harga_per_ton',
        ),
    ]
