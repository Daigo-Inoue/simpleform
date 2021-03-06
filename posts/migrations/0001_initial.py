# Generated by Django 2.1.15 on 2020-05-13 05:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='本文')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='作成日')),
            ],
            options={
                'db_table': 'posts',
            },
        ),
    ]
