# Generated by Django 3.0.7 on 2020-06-25 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0003_ordermodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermodel',
            old_name='name',
            new_name='username',
        ),
    ]