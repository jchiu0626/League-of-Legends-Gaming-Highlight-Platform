# Generated by Django 4.2.6 on 2023-11-18 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_details_nationality'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='sex',
            field=models.CharField(default='prefer not to say', max_length=50),
        ),
    ]
