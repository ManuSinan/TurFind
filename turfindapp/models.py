from django.db import models
from django.contrib.auth.models import AbstractUser

class LoginUser(AbstractUser):
    status_choices = (
        ('APPROVE', 'APPROVE'),
        ('REJECT', 'REJECT'),
    )
    status = models.CharField(choices=status_choices, max_length=20, default='PENDING', null=True, blank=True)
    user_type = models.CharField(max_length=50)

class User(models.Model):
    User_id = models.ForeignKey(LoginUser, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.user_name


class TurfOwner(models.Model):
    owner_id = models.ForeignKey(LoginUser, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.user_name


class Turf(models.Model):
    turf_id = models.ForeignKey(TurfOwner, on_delete=models.CASCADE)
    turf_features = models.CharField(max_length=20)
    price = models.IntegerField()
    details = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.details


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    login_user = models.ForeignKey(LoginUser, on_delete=models.CASCADE)
    book_date = models.CharField(max_length=50)
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE)
    payment_status = models.BooleanField(default=False)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    payment_method = models.CharField(max_length=50, null=True, blank=True)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'Booking {self.booking_id} by {self.login_user.username} on {self.book_date}'


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(LoginUser, on_delete=models.CASCADE)
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()

    def __str__(self):
        return f'Review by {self.user} for {self.turf}'