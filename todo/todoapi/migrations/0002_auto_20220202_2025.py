# Generated by Django 3.2.12 on 2022-02-02 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hero',
            old_name='alias',
            new_name='task',
        ),
        migrations.RemoveField(
            model_name='hero',
            name='name',
        ),
    ]
