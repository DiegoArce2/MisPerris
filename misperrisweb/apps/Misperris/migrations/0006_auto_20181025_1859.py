# Generated by Django 2.1.2 on 2018-10-25 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Misperris', '0005_auto_20181025_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perro',
            name='imagenPerro',
            field=models.CharField(default='sinImagen', max_length=30, verbose_name='imagenPerro'),
        ),
    ]