"""
URL configuration for EmployeeManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from employee.views import *

admin.site.site_header = "EMS Admin"
admin.site.site_title = "EMS Admin Portal"
admin.site.index_title = "Welcome to EMS Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('registration/', registration, name = 'registration'),
    path('employeeLogin/', employeeLogin, name = 'employeeLogin'),
    path('adminLogin/', adminLogin, name = 'adminLogin'),
    path('emp_home/', emp_home, name = 'emp_home'),
    path('profile/', profile, name = 'profile'),
    path('logout/', Logout, name = 'logout')
]
