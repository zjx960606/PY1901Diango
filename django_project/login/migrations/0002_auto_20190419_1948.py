# Generated by Django 2.2 on 2019-04-19 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='pub_data',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]