# Generated by Django 2.2 on 2019-04-29 06:38

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0004_auto_20190429_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('massage', tinymce.models.HTMLField()),
            ],
        ),
    ]