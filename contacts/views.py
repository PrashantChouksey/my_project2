from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
# Create your views here.
def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST.get('listing')
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "you have already made a inquery for this listing.")
                return redirect('/listing/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, email=email, name=name,
                          message=message, phone=phone,
                          user_id=user_id)
        contact.save()

        send_mail(
            'Contact Added Sucessfully.',
            'Thank you for adding. this email is just for testing emil service.',
            'prashant777ch@gmail.com',
            [realtor_email,'mr.prashant777ch@gmail.com'],
            fail_silently=False
        )

        messages.success(request, "Your request has been submitted, a realtor will get back to you soon")
        return redirect('/listing/'+listing_id)
