# Generated by Django 5.1.4 on 2025-01-02 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_remove_imageproduct_landscape_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageproduct',
            name='description',
        ),
        migrations.RemoveField(
            model_name='imageproduct',
            name='image',
        ),
        migrations.RemoveField(
            model_name='imageproduct',
            name='image_orientation',
        ),
        migrations.RemoveField(
            model_name='imageproduct',
            name='name',
        ),
        migrations.RemoveField(
            model_name='imageproduct',
            name='price',
        ),
    ]