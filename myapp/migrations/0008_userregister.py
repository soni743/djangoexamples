# Generated by Django 3.1.5 on 2021-02-10 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20210128_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Enter Name :')),
                ('email', models.EmailField(max_length=200, null=True, verbose_name='Enter Email :')),
                ('password', models.CharField(max_length=500, null=True, verbose_name='Enter Password')),
            ],
        ),
    ]