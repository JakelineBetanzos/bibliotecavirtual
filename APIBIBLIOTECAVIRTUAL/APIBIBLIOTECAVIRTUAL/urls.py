"""APIBIBLIOTECAVIRTUAL URL Configuration

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
from django.urls import path
from api.views import login, home, table, register, error, forgot_password, blank_page, buttons, cards, colors, borders, animations, other


urlpatterns = [
        # path('admin/', admin.site.urls),
    path('',login.as_view(),name='login'),
    path('home/',home.as_view(),name='home'),
    path('register/',register.as_view(),name='register'),
    path('error/',error.as_view(),name='error'),
    path('forgot_password/',forgot_password.as_view(),name= 'forgot_password'),
    path('blank_page',blank_page.as_view(),name= 'blank_page'),
    path('buttons/',buttons.as_view(),name= 'buttons'),
    path('cards/',cards.as_view(),name= 'cards'),
    path('colors',colors.as_view(),name= 'colors'),
    path('borders',borders.as_view(),name= 'borders'),
    path('animations',animations.as_view(),name= 'animations'),
    path('other',other.as_view(),name= 'other'),
    path('table',table.as_view(),name= 'table')
]
  