# Generated by Django 2.0.1 on 2022-06-12 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_admin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_id',
            field=models.CharField(max_length=150, null=True, verbose_name='User ID'),
        ),
    ]