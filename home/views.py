from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import contact as ContactModel
from django.contrib import messages

# Create your views here.
def index(request):
    context ={
        "variable1":"shivam is great",
        "variable2":"shiva is great"
    }

    return render(request,'index.html' , context)
    # return HttpResponse("this is homepage")
def about(request):
    return render(request,'about.html'  )
def services(request):
    return render(request,'services.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        # Use the ContactModel instead of contact to avoid naming conflict
        new_contact = ContactModel(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        new_contact.save()
        messages.success(request,'Your messege has been sent!')

    return render(request, 'contact.html')

     
