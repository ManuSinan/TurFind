"""
URL configuration for turfind project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from turfindapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path("login", views.login),
    path("reguser", views.reguser),
    path("regturfowner", views.regturfowner),
    path("profile", views.profile, name="profile"),
    path("booking", views.booking),
    path("rehome", views.homeagain, name='rehome'),
    path("addturf/", views.addturf, name="addturf"),
    path('turflist/', views.turflist, name='turflist'),
    path('editurf/<int:id>', views.editurf, name='editurf'),
    path("review/<int:id>", views.review, name="review"),
    path("logout/", views.logout,name="logout"),
    path("payment/<int:id>", views.payment, name='payment'),
    path("search", views.search),
    path("successpay/<int:id>", views.successpay, name='successpay'),
    path("history", views.history),
    path("booking", views.booking, name='booking'),
    path("deleteturf/<int:id>", views.deleteturf, name="deleteturf"),
    path('ownerprofile/', views.ownerprofile, name='ownerprofile'),
    path("ownerview/<int:id>", views.ownerview, name="ownerview"),
    path("ownersearch/", views.ownersearch, name="ownersearch"),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)