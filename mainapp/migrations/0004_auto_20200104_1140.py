# Generated by Django 3.0.1 on 2020-01-04 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_addproduct'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addproduct',
            old_name='productimage',
            new_name='product_image',
        ),
        migrations.RenameField(
            model_name='addproduct',
            old_name='productname',
            new_name='product_name',
        ),
        migrations.RemoveField(
            model_name='addproduct',
            name='productprice',
        ),
        migrations.AddField(
            model_name='addproduct',
            name='product_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]