from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
import requests
from django.core.mail import send_mail
from django.http import HttpResponse

# Create your views here.
def index(request):
    all_covers=Cover.objects.all()
    
    context={"all_covers":all_covers}
    return render(request,"index.html",context)

def cover(request):
    all_covers=Cover.objects.all()
    context={"all_covers":all_covers}
    return render(request,"cover.html",context)


   
def about(request):
    return render(request,"about.html")

def loginpage(request):
    if request.method=="POST":
        user_data=request.POST
        email=user_data.get("email")
        password=user_data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            # Log the user in if authentication is successful
            login(request, user)
            return redirect('/')  # Redirect to a page after successful login (replace 'home' with your desired page)
        else:
            # Authentication failed
            messages.error(request, "Invalid email or password.")
    return render(request,"login.html")

def signup(request):
    if request.method == "POST":
        user_data = request.POST
        name = user_data.get("name")
        email = user_data.get("email")
        password = user_data.get("password")
        
        # Check if the email already exists in the User model
        if not User.objects.filter(username=email).exists():
            # Create a new user and hash the password
            user = User(first_name=name, username=email)
            user.set_password(password)
            
            user.save()
             # Save the user to the database
            return redirect('/login')
        else:
            # Email already exists
            messages.error(request, "Email already exists. Please use a different email.")
            
    # If it's a GET request or the email already exists
    return render(request, "signup.html")
# def send_simple_message():
#   	        return requests.post(
#   		    "https://api.mailgun.net/v3/sandbox5fa91c73ca89427a95d2326ee79e1325.mailgun.org/messages",
#   		    auth=("api", "9a82b3879e391f23150794e9cbfa9c75-784975b6-35a476a4"),
#   		    data={"from": "Excited User <mailgun@sandbox5fa91c73ca89427a95d2326ee79e1325.mailgun.org>",
#   			"to": ["pateldhruvkumar010100@gmail.com", "YOU@sandbox5fa91c73ca89427a95d2326ee79e1325.mailgun.org"],
#   			"subject": "Hello",
#   			"text": "Testing some Mailgun awesomeness!"})

def send_simple_email(request):
    
    send_mail(
        subject="Hello from Django",
        message="This is a test email from your Django app.",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['pateldhruv010100@gmail.com'],  # List of email addresses
        
    )
    return HttpResponse(request,"Hello")

@login_required(login_url='/login')
def productcover(request,id):
    product=Cover.objects.get(id=id)

    context={"product":product}
    if request.method=="POST":
        user = request.user  
        order_details=request.POST
        address=order_details.get("address")
        postalcode=order_details.get("postalcode")
        paymenttype=order_details.get("paymenttype")
        # MH8B6CWK28FQS26A8C1GGVGG
        Orders.objects.create(username=user,phone=product.phone,price=product.price,address=address,postalcode=postalcode,paymenttype=paymenttype)
        
      
        send_simple_email()
        
        
        return redirect('/success')
     
    return render(request,"productcover.html",context)


def logout_view(request):
   
    
    logout(request)  # Logs out the user and clears the session
    return redirect('/') 
@login_required(login_url='/login')
def buy_now(request):
    return render(request,"success.html")
@login_required(login_url='/login')
def vieworder(request):
    user=request.user
    orders_details=Orders.objects.filter(username=user)
    context={"order_details":orders_details}
    return render(request,"vieworder.html",context)