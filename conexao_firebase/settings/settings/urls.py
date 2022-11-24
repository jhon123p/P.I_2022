"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
#admin , ifpi2022
from django.conf import settings ## import config feitas das bases
from django.conf.urls.static import static ## base que para importas os arquivos staticos
from django.contrib import admin
from django.urls import path , include
from app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('home/',views.home,name='home'),
    path('login', views.index , name = 'longin'),
    path('inscricoes/',views.inscricoes , name = 'inscricoes'),
    #path('login/',views.login,name='login'),
    path('questSo/' , views.questSo, name = 'questSo'),
    #path('logout/',views.logout_,name='logout'),
    #path('resultado/',views.resultado,name='resultado'),
    path('inscricoes/submit',views.resultado),
    #
    path('accounts/' , include('django.contrib.auth.urls'))

] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)

 