# Generated by Django 3.2.3 on 2021-06-23 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image4',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
