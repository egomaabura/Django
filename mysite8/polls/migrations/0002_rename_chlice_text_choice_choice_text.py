# Generated by Django 5.0.6 on 2024-06-05 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='chlice_text',
            new_name='choice_text',
        ),
    ]
