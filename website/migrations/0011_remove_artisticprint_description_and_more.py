# Generated by Django 5.1.4 on 2025-01-04 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_rename_payment_link_mounted_artisticprint_payment_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artisticprint',
            name='description',
        ),
        migrations.RemoveField(
            model_name='artisticprint',
            name='image',
        ),
        migrations.RemoveField(
            model_name='artisticprint',
            name='image_orientation',
        ),
        migrations.RemoveField(
            model_name='artisticprint',
            name='mounting',
        ),
        migrations.RemoveField(
            model_name='artisticprint',
            name='name',
        ),
        migrations.RemoveField(
            model_name='artisticprint',
            name='paper',
        ),
        migrations.RemoveField(
            model_name='artisticprint',
            name='price',
        ),
        migrations.RemoveField(
            model_name='artisticprint',
            name='size',
        ),
    ]
