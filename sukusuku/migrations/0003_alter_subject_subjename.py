# Generated by Django 3.2.8 on 2021-11-10 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sukusuku', '0002_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subjename',
            field=models.CharField(max_length=200),
        ),
    ]
