# Generated by Django 2.0.2 on 2019-09-25 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190925_0727'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='massage',
            new_name='message',
        ),
    ]