# Generated by Django 3.2.4 on 2021-06-14 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cahiercharge',
            name='cahierCharge',
            field=models.TextField(default='empty...'),
        ),
    ]