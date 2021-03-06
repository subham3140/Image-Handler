# Generated by Django 3.2.6 on 2021-08-31 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImagePro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagetitle', models.CharField(blank=True, default='new image', max_length=500, null=True)),
                ('image', models.ImageField(upload_to='images')),
                ('color_transform', models.CharField(blank=True, choices=[('l', 'L'), ('rbg', 'RBG'), ('cmyk', 'CMYK (cyan, magenta, yellow, black)')], max_length=500, null=True)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
