# Generated by Django 4.2.6 on 2023-11-04 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loloutplays', '0002_alter_loloutplaysstory_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loloutplaysstory',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
    ]
