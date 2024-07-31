from django.contrib.auth.models import AbstractUser
from django.db import models

class LoginUser(AbstractUser):
    status_choices = (
        ('APPROVE', 'APPROVE'),
        ('REJECT', 'REJECT'),
    )
    status = models.CharField(choices=status_choices, max_length=20, default='PENDING', null=True, blank=True)
    user_type = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, null=True, blank=True)


class User(models.Model):
    login_id = models.ForeignKey(LoginUser, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, blank=True)
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=gender_choices, null=True, blank=True)

    def __str__(self):
        return self.user_name


class TurfOwner(models.Model):
    owner_id = models.ForeignKey(LoginUser, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, blank=True)
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=gender_choices, null=True, blank=True)

    def __str__(self):
        return self.user_name

class Turf(models.Model):
    CATEGORY_CHOICES = [
        ('iconic', 'Iconic Stadiums'),
        ('economical', 'Economical Grass Choices'),
        ('eleven_a_side', '11-a-side Turf'),
        ('newly_added', 'Newly Added Turfs'),
    ]

    turf_id = models.ForeignKey(TurfOwner, on_delete=models.CASCADE, default=1)
    turf_name = models.CharField(max_length=100)
    price = models.IntegerField()
    details = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='newly_added')

    def __str__(self):
        return self.turf_name
class Booking(models.Model):
    login_id = models.ForeignKey(LoginUser, on_delete=models.CASCADE)
    book_datetime = models.DateTimeField(null=True, blank=True)
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE)
    payment_status = models.CharField(default="pending",max_length=100)
    payment_amount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'Booking {self.login_id.username} on {self.book_datetime}'


class Review(models.Model):
    login_id = models.ForeignKey(LoginUser, on_delete=models.CASCADE)
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()

    def __str__(self):
        return f'Review by {self.user} for {self.turf}'