# Generated by Django 5.1.4 on 2025-01-07 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learndjango', '0012_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='imag.png', null=True, upload_to='Profile'),
        ),
        migrations.DeleteModel(
            name='image',
        ),
    ]
