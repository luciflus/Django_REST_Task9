"""uber URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic import TemplateView

from account import views as acc_view
from service import views as serv_view

acc_router = DefaultRouter()
acc_router.register('register', acc_view.ProfileRegisterAPIView)
#acc_router.register('raiting', acc_view.ProfileRegisterAPIView)

serv_router = DefaultRouter()
serv_router.register('taxi', serv_view.TaxiViewSet)
serv_router.register('order', serv_view.OrderViewSet)
serv_router.register('raiting', serv_view.StatusTypeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/token', obtain_auth_token),
    path('api/auth/', include('rest_framework.urls')),

    path('api/account/', include(acc_router.urls)),
    path('api/service/', include(serv_router.urls)),
   # path('api/raiting/', include(serv_router.urls)),
]