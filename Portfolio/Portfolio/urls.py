"""
URL configuration for Portfolio project.

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
# views my app
from my_app import views as my_app_views
# views PORTFOLIO
from portfolio_app import views as portfolio_views
# view HERO
from hero_app import views as hero_views
# view ABOUT
from about_app import views as about_views
# view SKILLS
from skills_app import views as skills_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',my_app_views.home, name= 'home'),
    path('settings/', my_app_views.settings, name='settings'),
    
    path('settings/modify_hero/<int:id>', hero_views.modify_hero, name='modify-hero'),
    path('about-modify/<int:id>', about_views.about_modify, name='modify_about'),
    path('skills-modify/', skills_views.skills_modify, name='skills-modify'),
    
    path('portfolio_details/<int:id>', portfolio_views.portfolio_detail, name='details_portfolio'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
