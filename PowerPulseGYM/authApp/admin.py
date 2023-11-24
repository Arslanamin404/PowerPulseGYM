from django.contrib import admin
from .models import *


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'description')
# admin.site.register(Contact, ContactAdmin)


@admin.register(Enroll)
class EnrollAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','payment_status','due_date')


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','gender','expertise')


@admin.register(MembershipPlan)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'plan_name','plan_price')
