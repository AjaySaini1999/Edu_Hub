from django.shortcuts import render

# Create your views here.
from datetime import datetime
import email
from django.shortcuts import render, HttpResponse
from hub.models import Contact
from datetime import datetime
from django.contrib import messages
# Create your views here.


def index(request):

    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    context = None
    # Data BASE Connection here////
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        course = request.POST.get('course')

        contact = Contact(name=name, email=email, course=course,
                          phone=phone, date=datetime.today())
        contact.save()
        user_name = Contact.objects.last()
        context = {
            'user_name': user_name
        }
        messages.success(request, 'your registration is successfully done!')
    return render(request, 'contact.html', context)
