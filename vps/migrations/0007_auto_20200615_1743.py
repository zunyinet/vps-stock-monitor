# Generated by Django 2.2.5 on 2020-06-15 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vps', '0006_auto_20200615_1606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='companyId',
            new_name='company',
        ),
    ]
