# Generated by Django 4.0.4 on 2022-05-23 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=80, null=True)),
                ('f_name', models.CharField(max_length=80, null=True)),
                ('l_name', models.CharField(max_length=80, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
