from django.contrib import auth 
from django.contrib.auth.models import User 
from django.shortcuts import render, redirect 
# Create your views here. 
# 회원가입 
def signup(request): 
    if request.method == 'POST': 
        if request.POST['password1'] == request.POST['password2']: 
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user( 
                    username=request.POST['username'], 
                    password=request.POST['password1'],
                    email=request.POST['email'],
                    phonenum=request.POST['phonenum'],
                    ) 
                auth.login(request, user)
                return redirect('/')
        else:
            return render(request, 'signup.html', {'error':'Passwords must match'})
    else: 
        return render(request, 'signup.html') 

def login(request):
        if request.method == 'POST':
        # login.html에서 넘어온 username과 password를 각 변수에 저장하기.
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            phonenum = request.POST['phonenum']
        # 해당 username과 password와 일치하는 user 객체를 가져온다.
            user = auth.authenticate(request, username=username, password=password ,email=email, phoneum=phonenum)
        # 해당 user 객체가 존재한다면(객체가 존재하지 않는다면 none을 반환할 텐데, none이 not이니까 존재한다면!)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                return render(request, 'login.html', {'error': 'username or password is incorrect.'})
        else:
            return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
         auth.logout(request)
         return redirect('/')
    return render(request, 'signup.html')  