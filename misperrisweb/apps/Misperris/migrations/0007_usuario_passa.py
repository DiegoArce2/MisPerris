# Generated by Django 2.1.2 on 2018-10-26 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Misperris', '0006_auto_20181025_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='passa',
            field=models.CharField(default='pass', max_length=20, verbose_name='passa'),
        ),
    ]
