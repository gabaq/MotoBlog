# Generated by Django 4.2.2 on 2023-07-15 04:12

import Users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0007_profile_country_profile_dateofbirth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=Users.models.user_avatar_path),
        ),
    ]