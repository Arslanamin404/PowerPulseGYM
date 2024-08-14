# Generated by Django 4.2.5 on 2024-08-13 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0018_alter_enroll_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enroll',
            name='payment_status',
            field=models.CharField(choices=[('unpaid', 'Unpaid'), ('paid', 'Paid')], default='unpaid', max_length=10),
        ),
    ]
