# Generated by Django 2.1.2 on 2018-10-25 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Misperris', '0003_auto_20181025_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perro',
            name='imagen',
            field=models.CharField(default='sinImagen', max_length=30, verbose_name='imagen'),
        ),
    ]