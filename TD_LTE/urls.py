"""TD_LTE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from Log.views import import_table_from_excel
from Log.views import show_data
from Log.views import login
urlpatterns = [
    #path('admin/', admin.site.urls),
    #url(r'^test/', import_table_from_excel),
    #url(r'^stest/', show_data),
    url(r'^login/', login, name="loginIndex")
    #url(r'^test/', import_table_from_excel),
]
