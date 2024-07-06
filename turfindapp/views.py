from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from .models import LoginUser, User, Turf


def home(request):
    return render(request, 'home.html')

def reguser(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if LoginUser.objects.filter(username=username, user_type='User').exists():
            return render(request, 'signup.html', {'message': 'Username already exists'})

        if password != confirm_password:
            return render(request, 'signup.html', {'message': 'Passwords do not match'})

        try:
            login_data = LoginUser.objects.create_user(username=username, password=password, user_type='User')

            user_data = User.objects.create(login_id=login_data, user_name=username, email=email, phone=phone, password=password)
            return redirect(login)
        except Exception as e:
            return render(request, 'signup.html', {'message': f'Error occurred: {str(e)}'})
    else:
        return render(request, 'signup.html')

def regturfowner(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if LoginUser.objects.filter(username=username, user_type='TurfOwner').exists():
            return render(request, 'signup_turf_owner.html', {'message': 'Username already exists'})

        if password != confirm_password:
            return render(request, 'signup_turf_owner.html', {'message': 'Passwords do not match'})

        try:
            login_data = LoginUser.objects.create_user(username=username, password=password, user_type='TurfOwner')

            user_data = User.objects.create(login_id=login_data, user_name=username, email=email, phone=phone, password=password)
            return redirect(login)
        except Exception as e:
            return render(request, 'signup_turf_owner.html', {'message': f'Error occurred: {str(e)}'})
    else:
        return render(request, 'signup_turf_owner.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            if user.user_type == "User" or user.user_type == "TurfOwner":
                return redirect(homeagain)
            else:
                return render(request, 'login.html', {'message': "Unknown user type"})
        else:
            return render(request, 'login.html', {'message': 'Invalid credentials'})
    else:
        return render(request, 'login.html')

def addturf(request):
    if "id" in request.session:
        id = request.session["id"]
        if request.method == 'POST':
            turf_name = request.POST['turf_name']
            location = request.POST['location']
            details = request.POST['details']
            turf_photo = request.FILES['turf_photo']
            data2 = Turf.objects.create(turf_name=turf_name, location=location, details=details, image=turf_photo)
            data2.save()
            return redirect(homeagain)
        else:
            return render(request,'addturf.html')
    else:
        return redirect(homeagain)

def profile(request):
    login_user = LoginUser.objects.get(id=request.user.id)
    user_data = User.objects.get(login_id=login_user)

    if request.method == "POST":
        login_user.username = request.POST.get('user_name', login_user.username)
        login_user.email = request.POST.get('email', login_user.email)
        login_user.phone = request.POST.get('phone_no', login_user.phone)
        login_user.date_of_birth = request.POST.get('date_of_birth', login_user.date_of_birth)
        login_user.gender = request.POST.get('gender', login_user.gender)
        login_user.save()
        return redirect(profile)
    else:
        return render(request, 'profile.html', {'data': user_data})
def booking(request):
    return render(request, 'booking.html')

def homeagain(request):
    query = request.GET.get('turflist')
    if query:
        turfs = Turf.objects.filter(details__icontains=query)
    else:
        turfs = Turf.objects.all()
    return render(request, 'redirecthome.html', {'turfs': turfs})


