# Generated by Django 5.0.4 on 2024-04-20 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_category_alter_item_id_alter_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]