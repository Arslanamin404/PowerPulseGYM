from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=12)
    description = models.TextField()


class Enroll(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    gender = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    date_of_birth = models.DateField()
    membership_plan = models.CharField(max_length=200)
    trainer = models.CharField(max_length=100)
    address = models.TextField()
    payment_status = models.CharField(max_length=80, null=True, blank=True)
    payment_paid = models.IntegerField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class Trainer(models.Model):
    name = models.CharField(max_length=80)
    gender = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    expertise = models.CharField(max_length=50)  # expert-in
    salary = models.PositiveIntegerField()


class MembershipPlan(models.Model):
    plan_name = models.CharField(max_length=150)
    plan_price = models.PositiveIntegerField()
