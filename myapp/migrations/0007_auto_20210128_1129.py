# Generated by Django 3.1.5 on 2021-01-28 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20210125_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Full Name :')),
                ('email', models.EmailField(max_length=200, verbose_name='Email :')),
                ('purpose', models.CharField(choices=[('Purpose1', 'Purpose1'), ('Purpose2', 'Purpose2')], max_length=200, verbose_name='Purpose :')),
                ('msg', models.TextField(max_length=1000, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
