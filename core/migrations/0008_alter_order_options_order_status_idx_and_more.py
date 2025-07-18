# Generated by Django 5.2.1 on 2025-06-07 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_service_options_alter_master_photo_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-date_created'], 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AddIndex(
            model_name='order',
            index=models.Index(fields=['status'], name='status_idx'),
        ),
        migrations.AddIndex(
            model_name='order',
            index=models.Index(fields=['date_created'], name='created_at_idx'),
        ),
    ]
