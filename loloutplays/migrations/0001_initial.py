# Generated by Django 4.2.6 on 2023-11-04 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoloutplaysStory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('video', models.FileField(upload_to='videos/')),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('comments', models.TextField()),
            ],
        ),
    ]
