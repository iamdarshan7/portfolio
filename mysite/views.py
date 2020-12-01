from django.shortcuts import render
from .models import Portfolio1, Portfolio2, ContactInfo
from .forms import ContactInfoForm  
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def home(request):
    return render(request, 'mysite/index.html')


def actor(request):
    datas = Portfolio1.objects.all()
    data2 = Portfolio2.objects.all()
    
    context = {
        "datas":datas,
        "data2":data2
    }

    return render(request, 'mysite/index.html' , context)



def contact(request):
    success = False
    datas = Portfolio1.objects.all()
    data2 = Portfolio2.objects.all()

    if request.method == "POST":
        fm = ContactInfoForm(request.POST)
        message1 = request.POST['name']
        message2 = request.POST['email']
        message3 = request.POST['phone']
        message4 = request.POST['message']

        message = "Name: " + message1 + "\n" + "Email: " + message2 + "\n" + "Phone: " + message3 + "\n" + "Message : " + message4
        if fm.is_valid():
            fm.save()
            send_mail(
                "Contact Query",
                message,
                settings.EMAIL_HOST_USER,
                ['darshanthapa872@gmail.com'],
                fail_silently=False,    
            )
            messages.add_message(request, messages.SUCCESS, "Thank you for your message")
            success = True
            fm = ContactInfoForm()
    else:

        fm = ContactInfoForm()
    return render(request, 'mysite/index.html', {'form': fm, "success": success, 'datas': datas, 'data2': data2})            