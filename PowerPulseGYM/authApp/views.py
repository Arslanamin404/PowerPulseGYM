from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import *
from django.core.mail import send_mail
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.conf import settings


def home(request):
    return render(request, "index.html")


def signup(request):
    if request.method == 'POST':
        name = request.POST['fullname']
        username = request.POST['number']  # store number as username
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.warning(
                    request, "This Phone number is already registered.")
                return redirect('signup')
            if len(username) > 10 or len(username) < 10:
                messages.warning(
                    request, "Invalid Phone number! Please enter a valid Phone Number.")
                return redirect('signup')
            if User.objects.filter(email=email).exists():
                messages.warning(request, "This email is already registered.")
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    first_name=name, username=username, email=email, password=password)
                user.save()

                # Define the context for the template
                context = {
                    'name': name,
                }

                # Load your custom HTML template
                html_template = get_template('email.html')

                # Render the HTML template with the context
                html_content = html_template.render(context, request)

                # Email Subject
                subject = 'Welcome to Power Pulse Gym - Let\'s Ignite Your Fitness Journey!'

                # Sender and recipient email addresses
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [email,]

                # Create the EmailMultiAlternatives object
                msg = EmailMultiAlternatives(
                    subject, '', from_email, recipient_list)
                msg.attach_alternative(html_content, "text/html")

                # Send the email
                msg.send()

                messages.success(
                    request, "Congratulations! You have registered successfully. Please Login!")
                return redirect('login')
        else:
            messages.warning(request, "Password does not match!")
            return redirect('signup')
    else:
        return render(request, "signup.html")


def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['number']  # store number as username
            password = request.POST['password']

            user = auth.authenticate(username=username,
                                     password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                messages.warning(
                    request, "Invalid Login credentials! Please check and try again or Signup if you are a new member.")
                return redirect('login')
        else:
            return render(request, "login.html")
    else:
        return redirect('home')


def logout(request):
    auth.logout(request)
    return redirect('home')


def contact(request):
    if request.method == 'POST':
        name = request.POST['fullname']
        phone = request.POST['number']
        email = request.POST['email']
        description = request.POST['description']

        contactUs = Contact(name=name, phone=phone,
                            email=email, description=description)
        contactUs.save()
        messages.info(
            request, "Thanks for Contacting us we will get back to you soon!")
        return redirect('contact')
    else:
        return render(request, "contact.html")


def enroll_now(request):
    if request.user.is_authenticated:
        memberships = MembershipPlan.objects.all()
        trainers = Trainer.objects.all()
        context = {'memberships': memberships, 'trainers': trainers}

        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['number']
            gender = request.POST['gender']
            dob = request.POST['dob']
            membership_plan = request.POST['membership_plan']
            trainer = request.POST['trainer']
            address = request.POST['address']
            print(name)
            if len(phone) > 10 or len(phone) < 10:
                messages.warning(
                    request, "Invalid Phone number! Please enter a valid Phone Number.")
                return redirect('enroll')
            else:
                # Check if the user already has an enrollment
                enrollment = Enroll.objects.filter(user=request.user).order_by('-id').first()

                if enrollment:
                    # Update the existing enrollment details
                    enrollment.name = name
                    enrollment.email = email
                    enrollment.phone = phone
                    enrollment.gender = gender
                    enrollment.date_of_birth = dob
                    enrollment.membership_plan = membership_plan
                    enrollment.payment_status = "Unpaid"
                    enrollment.payment_paid = None
                    enrollment.due_date =None
                    enrollment.trainer = trainer
                    enrollment.address = address
                    enrollment.save()

                    messages.success(
                        request, "Your enrollment details have been updated successfully!")
                else:
                    # Create a new enrollment
                    enrollment = Enroll(user=request.user,  # Associate with the logged-in user
                                        name=name,
                                        email=email,
                                        phone=phone,
                                        gender=gender,
                                        date_of_birth=dob,
                                        membership_plan=membership_plan,
                                        trainer=trainer,
                                        address=address)
                    enrollment.save()


                messages.success(
                    request, "Congratulations! You have enrolled successfully. Thanks for joining us!")
                return redirect('enroll')
        else:
            return render(request, "enroll.html", context)
    else:
        messages.warning(request, "Please Login and Try Again!")
        return redirect('login')


def profile(request):
    if request.user.is_authenticated:
        try:
            user = Enroll.objects.filter(phone=request.user.username).order_by('-id').first()
            print(user.name, user.email)
            context = {'user': user}
            return render(request, "profile.html", context)
        except Enroll.DoesNotExist:
            messages.warning(
                request, "You are not enrolled. Please enroll to view your profile.")
            return redirect('enroll')
    else:
        messages.warning(
            request, "Please Login first and Try Again to view your profile!")
        return redirect('login')


def about(request):
    return render(request, "about.html")
