# Generated by Django 4.2.6 on 2023-11-06 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_productcategory_slug_alter_productcategory_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(max_length=30),
        ),
    ]
