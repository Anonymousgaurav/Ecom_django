# Generated by Django 4.1.4 on 2023-01-02 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_customer_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
