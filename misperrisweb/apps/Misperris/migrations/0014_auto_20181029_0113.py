# Generated by Django 2.1.2 on 2018-10-29 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Misperris', '0013_auto_20181029_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perro',
            name='imagenPerro',
            field=models.FileField(upload_to='perros/'),
        ),
    ]
