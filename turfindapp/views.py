from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse
from .models import LoginUser, User, Turf, TurfOwner, Booking

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

            user_data = TurfOwner.objects.create(owner_id=login_data, user_name=username, email=email, phone=phone, password=password)
            return redirect(login)
        except Exception as e:
            return HttpResponse(e)
    else:
        return render(request, 'signup_turf_owner.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            if user.user_type == "User":
                return redirect(homeagain)
            elif user.user_type == "TurfOwner":
                return redirect(addturf)
            else:
                return render(request, 'login.html', {'message': "Unknown user type"})
        else:
            return render(request, 'login.html', {'message': 'Invalid credentials'})
    else:
        return render(request, 'login.html')


def addturf(request):
    owner = LoginUser.objects.get(id=request.user.id)
    data = TurfOwner.objects.get(owner_id=owner)
    if request.method == 'POST':
        turf_name = request.POST['turf_name']
        location = request.POST['location']
        details = request.POST['details']
        image = request.FILES['image']
        price = request.POST['price']
        category = request.POST['category']

        newturf = Turf.objects.create(turf_id=data, turf_name=turf_name, location=location, details=details, image=image, price=price, category=category)
        newturf.save()

        return redirect(turflist)
    else:
        return render(request, 'addturf.html',{'turf': Turf})

def profile(request):
    login_user = LoginUser.objects.get(id=request.user.id)
    user_data = User.objects.get(login_id=login_user)

    if request.method == "POST":
        login_user.username = request.POST.get('user_name', login_user.username)
        login_user.email = request.POST.get('email', login_user.email)
        login_user.phone = request.POST.get('phone_no', login_user.phone)
        login_user.save()

        user_data.user_name = login_user.username
        user_data.email = login_user.email
        user_data.phone = login_user.phone
        user_data.date_of_birth = request.POST.get('date_of_birth', user_data.date_of_birth)
        user_data.gender = request.POST.get('gender', user_data.gender)
        user_data.save()

        return redirect(profile)
    else:
        return render(request, 'profile.html', {'data': user_data})

def booking(request):
    login_user = LoginUser.objects.get(id=request.user.id)
    if request.method == 'POST':
        turf_name = request.POST['turf_name']
        location = request.POST['location']
        details = request.POST['details']
        image = request.FILES['image']
        price = request.POST['price']
        category = request.POST['category']

        Booking.objects.create(login_id=login_user, turf_name=turf_name, location=location, details=details,image=image, price=price, category=category)
    return render(request, 'booking.html')

def homeagain(request):
    iconic_stadiums = Turf.objects.filter(category='iconic')
    economical_grass = Turf.objects.filter(category='economical')
    eleven_a_side = Turf.objects.filter(category='eleven_a_side')
    newly_added = Turf.objects.filter(category='newly_added')

    context = {
        'iconic_stadiums': iconic_stadiums,
        'economical_grass': economical_grass,
        'eleven_a_side': eleven_a_side,
        'newly_added': newly_added,
    }
    return render(request, 'redirecthome.html', context)

def turflist(request):
    owner = TurfOwner.objects.get(owner_id=request.user)
    turfs = Turf.objects.filter(turf_id=owner)
    return render(request, 'myturfpage.html', {'turfs': turfs})

def editurf(request, id):
    owner = TurfOwner.objects.get(owner_id=request.user)
    turf = Turf.objects.filter(turf_id=owner, id=id).first()
    if request.method == 'POST':
        turf.turf_name = request.POST['turf_name']
        turf.location = request.POST['location']
        turf.details = request.POST['details']

        if 'image' in request.FILES:
            turf.image = request.FILES['image']

        turf.price = request.POST['price']
        turf.save()
        return redirect(turflist)
    else:
        return render(request, 'editurf.html', {'turf': turf})

def review(request, id):
    user = LoginUser.objects.get(id=request.user.id)
    turf = Turf.objects.get(id=id)
    if request.method == 'POST':
        day = request.POST['day']
        booking = Booking.objects.create(login_id=user, book_datetime=day, turf=turf, payment_amount=turf.price)
        booking.save()
        return redirect(payment, id=id)
    else:
        return render(request, 'review.html', {'turf': turf})
def logout(request):
    auth_logout(request)
    return redirect(login)

def search(request):
    query = request.GET.get('turf_name')
    if query:
        turfs = Turf.objects.filter(turf_name__icontains=query)
    else:
        turfs=Turf.objects.all()
    return render(request,'redirecthome.html', {'turfs': turfs})

def payment(request, id):
    turf = Turf.objects.get(id=id)
    if request.method == 'POST':
        return redirect('successpay', id=id)
    else:
        return render(request, 'payment.html', {'turf': turf})

def successpay(request, id):
    turf = Turf.objects.get(id=id)
    return render(request, 'paysuccess.html', {'turf': turf})

def history(request):
    login_user = LoginUser.objects.get(id=request.user.id)
    bookings = Booking.objects.filter(login_id=login_user)
    return render(request, 'history.html', {'bookings': bookings})


