# Generated by Django 4.1.7 on 2023-03-07 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0003_alter_women_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='women',
            options={'ordering': ('cat', 'title'), 'verbose_name_plural': 'Известные женщины'},
        ),
    ]