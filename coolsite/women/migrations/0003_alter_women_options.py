# Generated by Django 4.1.7 on 2023-03-04 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_alter_women_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='women',
            options={'ordering': ('-time_update', 'title'), 'verbose_name_plural': 'Известные женщины'},
        ),
    ]
