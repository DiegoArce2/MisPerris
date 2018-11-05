# Generated by Django 2.1.2 on 2018-10-25 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Misperris', '0002_perro_nombreperro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perro',
            name='idImagen',
        ),
        migrations.AddField(
            model_name='perro',
            name='imagen',
            field=models.CharField(default='nn', max_length=30, verbose_name='imagen'),
        ),
        migrations.DeleteModel(
            name='imagen',
        ),
    ]
