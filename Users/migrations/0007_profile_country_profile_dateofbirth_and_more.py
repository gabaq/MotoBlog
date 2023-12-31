# Generated by Django 4.2.2 on 2023-07-14 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='dateOfBirth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
