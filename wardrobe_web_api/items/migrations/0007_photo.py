# Generated by Django 5.0.4 on 2024-04-20 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_alter_category_id_alter_item_category_alter_item_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='item_photos/')),
            ],
        ),
    ]