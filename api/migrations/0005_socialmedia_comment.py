# Generated by Django 5.1.1 on 2024-09-26 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_socialmedia_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmedia',
            name='comment',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
