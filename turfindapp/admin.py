from django.contrib import admin
from .models import LoginUser, Turf, TurfOwner, User, Booking, Review

admin.site.register(LoginUser)
admin.site.register(Turf)
admin.site.register(TurfOwner)
admin.site.register(User)
admin.site.register(Booking)
admin.site.register(Review)