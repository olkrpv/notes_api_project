# Generated by Django 3.2.16 on 2023-07-27 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_follow'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='unique_user_following'),
        ),
    ]
