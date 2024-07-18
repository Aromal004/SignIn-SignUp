
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login as auth_login,logout
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

User=get_user_model()

#Create user Serialer
@api_view(['GET'])
def getData(request):
    items=User.objects.all()
    serializer=UserSerializer(items,many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def allData(request):
#     response=requests.get('http://127.0.0.1:8000/get-data').json()
#     return render(request,'allData.html',{'items':response})

@api_view(['POST'])
def addData(request):
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Create your views here.
def register(request):
    if request.method== 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']        
        email=request.POST['email']
        password=request.POST['password']
        phone=request.POST['phone']
        gender=request.POST['gender']
        if User.objects.filter(phone=phone).exists():
            messages.info(request,'User Already Exists!!')
            return redirect('/')
        user=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,password=password,phone=phone,gender=gender)
        user.save() 
        return render(request,'welcome.html',{'message':'WELCOME  '+first_name})
    else:
        return render(request, 'Form.html')




def login(request):
    if request.method== 'POST':
        phone=request.POST['phone']
        password=request.POST['password']
        if(phone=='' or password==''):
            messages.info(request,'Please enter the Phone Number and Password')
            return redirect('/')    
        else:
            if User.objects.filter(phone=phone).exists():
                user=authenticate(request,phone=phone,password=password)
                if user is not None:
                    auth_login(request,user)
                    return render(request,'welcome.html',{'message':'WELCOME  '+user.first_name})
                else:
                    messages.info(request,'Wrong Password! ')
                    messages.info(request,'Enter registered Phone Number and Password')
                    return redirect('/')
            else:
                messages.info(request,'Not an existing User! ')
                messages.info(request,'Enter registered Phone Number and Password')
                return redirect('/')
    else:
        return render(request,'Login.html')
    

def user_logout(request):
    logout(request)
    return redirect('/')