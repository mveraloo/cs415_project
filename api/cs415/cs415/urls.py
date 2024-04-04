"""
URL configuration for cs415 project.

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
from cs415 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.Login.as_view()),
    path('carts/', views.CartAPIView.as_view()),
    path('orders/', views.OrdersAPIView.as_view()),
    path('packages/', views.PackageAPIView.as_view()),
    path('payments/', views.PaymentAPIView.as_view()),
    path('paymenttypes/', views.PaymenttypeAPIView.as_view()),
    path('useraccounts/', views.UseraccountAPIView.as_view()),
    path('userprofile/', views.UserprofileAPIView.as_view()),
    # path('userprofiles/userprofile/<int:id>/', views.GetSingleUserProfileAPIView.as_view()),
    path('useraccounts/useraccount/<int:id>/', views.GetSingleUserAccountAPIView.as_view()),
    path('orders/order/<int:id>/', views.GetSingleOrderAPIView.as_view()),
]

