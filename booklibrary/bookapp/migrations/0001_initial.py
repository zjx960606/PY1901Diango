# Generated by Django 2.2 on 2019-04-26 08:36

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.IntegerField(max_length=20)),
                ('title', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('press', models.CharField(max_length=20)),
                ('publishers', models.CharField(max_length=20)),
                ('pub_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='StuUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('stu_id', models.IntegerField(blank=True, max_length=20, null=True)),
                ('college', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bor_time', models.DateTimeField(auto_now_add=True)),
                ('re_time', models.DateTimeField(blank=True, null=True)),
                ('borrow_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapp.BookInfo')),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapp.StuUser')),
            ],
        ),
    ]
