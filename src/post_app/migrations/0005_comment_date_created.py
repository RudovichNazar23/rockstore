# Generated by Django 4.2.3 on 2023-08-15 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0004_remove_post_rating_post_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_created',
            field=models.DateField(auto_now=True),
        ),
    ]
