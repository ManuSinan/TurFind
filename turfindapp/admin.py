from django.contrib import admin
from .models import LoginUser, Turf, TurfOwner, User

admin.site.register(LoginUser)
admin.site.register(Turf)
admin.site.register(TurfOwner)
admin.site.register(User)
