# Generated by Django 2.1.4 on 2018-12-24 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientebd',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_clientes'),
        ),
    ]
