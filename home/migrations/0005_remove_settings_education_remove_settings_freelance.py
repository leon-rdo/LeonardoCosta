# Generated by Django 5.0.1 on 2024-02-25 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_text_subtext'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='education',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='freelance',
        ),
    ]
