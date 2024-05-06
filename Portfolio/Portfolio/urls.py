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
# view SERVICES
from services_app import views as services_views
# view TESTIMONIALS
from testimonials_app import views as testimonials_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',my_app_views.home, name= 'home'),
    path('settings/', my_app_views.settings, name='settings'),
    # HERO
    path('settings/modify_hero/<int:id>', hero_views.modify_hero, name='modify-hero'),
    path('settings/about-modify/<int:id>', about_views.about_modify, name='modify_about'),
    # SKILLS
    path('settings/skills-settings/', skills_views.skills_settings, name='skills-settings'),
    path('settings/skills-settings/modify/<int:id>', skills_views.skills_modify, name='skills-modify'),
    path('settings/skills-settings/destroy/<int:id>', skills_views.delete_skill, name='skills-delete'),
    path('settings/skills-settings/create', skills_views.create_skill, name='skills-create'),
    # SERVICES
    path('settings/services-modify/', services_views.services_modify, name= 'services-modify'),
    # TESTIMONIALS
    path('settings/testimonials_settings/', testimonials_views.testimonial_settings, name='testimonial_settings'),
    path('testimonials_settings/modify/<int:id>', testimonials_views.testimonial_modify, name='testimonial_modify'),
    path('testimonials_settings/destroy/<int:id>', testimonials_views.delete_testimonial, name='testimonial_delete'),
    path('testimonials_settings/create', testimonials_views.create_testimonial, name='testimonial_create'),
    # PORTFOLIO
    path('portfolio_details/<int:id>', portfolio_views.portfolio_detail, name='details_portfolio'),
    path('settings/portfolio', portfolio_views.portfolio_settings, name='portfolio_settings'),
    path('settings/portfolio/destroy/<int:id>', portfolio_views.delete_portfolio, name='portfolio_delete'),
    path('settings/portfolio/create', portfolio_views.create_portfolio, name='portfolio_create'),
    path('settings/portfolio/<int:id>', portfolio_views.portfolio_modify, name='portfolio_modify'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
