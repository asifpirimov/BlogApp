# Generated by Django 5.0.1 on 2024-02-10 16:59

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_myapp_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myapp',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='myapp',
            name='image',
            field=models.ImageField(upload_to='myapps'),
        ),
    ]