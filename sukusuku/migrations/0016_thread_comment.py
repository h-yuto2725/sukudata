# Generated by Django 4.0 on 2021-12-21 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sukusuku', '0015_alter_group_groupid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('threadid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=100)),
                ('flag', models.CharField(max_length=1)),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sukusuku.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='user', max_length=100)),
                ('comment', models.CharField(max_length=100)),
                ('flag', models.BooleanField(default=True)),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sukusuku.thread')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sukusuku.user')),
            ],
        ),
    ]