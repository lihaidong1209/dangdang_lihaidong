# Generated by Django 2.0.6 on 2019-05-25 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50, null=True, verbose_name='用户名')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='昵称')),
                ('password', models.CharField(blank=True, max_length=100, null=True, verbose_name='密码')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('code', models.CharField(max_length=256, verbose_name='用户注册码')),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 't_email',
            },
        ),
    ]
