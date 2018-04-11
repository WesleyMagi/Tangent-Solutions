"""Interview_Assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import HomeTemplateView, LoginView, WhoAmI, LogoutViewEx, EmployeeView,FindAFriendView,CompanyStatsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('who_am_i/', WhoAmI.as_view(), name='who_am_i', ),
    path('rest-auth/logout/', LogoutViewEx.as_view(), name='rest_logout', ),
    path('rest-auth/login/', LoginView.as_view(), name='rest_login', ),
    path('employee/', EmployeeView.as_view(),name='employee',),
    path('find_a_friend/', FindAFriendView.as_view(),name='find_a_friend'),
    path('company_stats',CompanyStatsView.as_view(),name='company_stats'),
    path('', HomeTemplateView.as_view(), name='home', ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
