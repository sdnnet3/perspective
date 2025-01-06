# Generated by Django 5.1.4 on 2025-01-04 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_remove_artisticprint_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artisticprint',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artisticprint',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/prints/'),
        ),
        migrations.AddField(
            model_name='artisticprint',
            name='image_orientation',
            field=models.CharField(choices=[('portrait', 'Portrait'), ('landscape', 'Landscape')], default='portrait', max_length=10),
        ),
        migrations.AddField(
            model_name='artisticprint',
            name='mounting',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='artisticprint',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artisticprint',
            name='paper',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='artisticprint',
            name='price',
            field=models.DecimalField(decimal_places=2, default=2.0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artisticprint',
            name='size',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
