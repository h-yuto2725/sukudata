# Generated by Django 3.2.8 on 2021-11-10 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sukusuku', '0004_rename_subjename_subject_subjectname'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='subjectnote',
            field=models.CharField(default='aaa', max_length=200),
            preserve_default=False,
        ),
    ]
