# Generated by Django 4.2.5 on 2023-11-19 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0003_alter_membershipplan_plan_price_alter_trainer_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='enroll',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='enroll',
            name='payment_paid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='enroll',
            name='payment_status',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
