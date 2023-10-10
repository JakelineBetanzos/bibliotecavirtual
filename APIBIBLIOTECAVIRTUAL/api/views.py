import json
from rest_framework.views import APIView
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# class login(APIView):

#     login="login.html"
#     def get(self,request): 
#         return render(request,self.login)
    
#     def post(self,request):
#         username = request.POST['username']
#         password = request.POST['password']
#         print(username, password)
#         user = authenticate(request, username = username , password = password)

#         if user is not None:
#             if user.is_active:
#                 login(request,user)
#                 messages.success(request, 'Inicio de Sesion Exitoso')
#                 return redirect('home')
#         else: 
#             return render(request, self.login)
        
class home(APIView):
    home="index.html"
    def get(self,request): 
        return render(request,self.home)


class login(APIView):
    login="login.html"
    def get(self,request): 
        return render(request,self.login)
    
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username = username , password = password)

        if user is not None:
            if user.is_active:
                login(request,user)
                messages.success(request, 'Inicio de Sesion Exitoso')
                return redirect('home')
        else: 
            return render(request, self.login)



class register(APIView):
    register="register.html"
    def get(self,request): 
        return render(request,self.register)
    def post (self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user =form.save()
            login(request, user)
            subject = 'Confirmacion de registro'
            message = 'Registro exitoso'
            from_email ='noreply@example.com'
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list)
            return redirect('index.html')
        return render(request, self.login, context={'form':form})
            
    
class error(APIView):
    error="404.html"
    def get(self,request): 
        return render(request,self.error)

class forgot_password(APIView):
    forgot_password="forgot-password.html"
    def get(self,request): 
        return render(request,self.forgot_password)

class blank_page(APIView):
    blank_page="blank.html"
    def get(self,request): 
        return render(request,self.blank_page)
class buttons(APIView):
    buttons="buttons.html"
    def get(self,request): 
        return render(request,self.buttons)

class cards(APIView):
    cards="cards.html"
    def get(self,request): 
        return render(request,self.cards)

class colors(APIView):
    colors="colors.html"
    def get(self,request): 
        return render(request,self.colors)
    
class borders(APIView):
    borders="utilities-border.html"
    def get(self,request): 
        return render(request,self.borders)

class animations(APIView):
    animations="utilities-animation.html"
    def get(self,request): 
        return render(request,self.animations)

class other(APIView):
    other="utilities-other.html"
    def get(self,request): 
        return render(request,self.other)
class table(APIView):
    table="data_table.html"
    def get(self,request):
        return render(request,self.table)

