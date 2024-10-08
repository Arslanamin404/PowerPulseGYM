# Generated by Django 4.2.5 on 2023-11-19 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='enroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('date_of_birth', models.DateField()),
                ('membership_plan', models.CharField(max_length=200)),
                ('trainer', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MembershipPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=150)),
                ('plan_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('gender', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('expertise', models.CharField(max_length=50)),
            ],
        ),
    ]
