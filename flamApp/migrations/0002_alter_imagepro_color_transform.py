# Generated by Django 3.2.6 on 2021-08-31 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flamApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagepro',
            name='color_transform',
            field=models.CharField(blank=True, choices=[('rotate 90', 'ROTATE 90'), ('rotate 180', 'ROTATE 180'), ('rotate 270', 'ROTATE 270')], max_length=500, null=True),
        ),
    ]