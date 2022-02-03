# Generated by Django 3.2.12 on 2022-02-02 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0002_auto_20220202_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=100)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Hero',
        ),
    ]
