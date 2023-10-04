"""
URL configuration for proj1 project.

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
from django.conf import settings
from django.conf.urls.static import static
from test1 import views
from django.urls import path





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
     path('myhome',views.myhome,name='myhome'),
    path('<int:pid>', views.details, name='details'),
    path('signupuser/',views.signupuser,name='signupuser'),
    path('loginuser/',views.loginuser,name='loginuser'),
    path('logoutuser/',views.logoutuser,name='logoutuser'),
    path('allproducts',views.allproducts,name='allproducts'),
    path('contact/', views.contact,name='contact'),
    path('contact/add_record',views.add_record,name='add_record'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('search',views.search,name='search'),
    path('show/',views.show,name='show'),
    

    
    
]
    



if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
