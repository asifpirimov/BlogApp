# Generated by Django 4.2.7 on 2024-02-15 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_myapp_catrgory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myapp',
            old_name='catrgory',
            new_name='category',
        ),
    ]
