# Generated by Django 2.0.1 on 2022-06-12 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_admin', '0007_auto_20220612_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uservouchers',
            name='status',
        ),
        migrations.AddField(
            model_name='uservouchers',
            name='voucher_status',
            field=models.CharField(blank=True, choices=[('used', 'used'), ('active', 'active')], max_length=32, null=True, verbose_name='Voucher Status'),
        ),
    ]
