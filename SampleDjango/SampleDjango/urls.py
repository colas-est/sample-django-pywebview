"""SampleDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from main.views import ListIntervention, DoneIntervention, LifeReport

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^interventions/$', ListIntervention.as_view(), name='url_list_intervention'),
    url(r'^interventions/done/$', DoneIntervention.as_view(), name='url_done_intervention'),
    url(r'^life_report/$', LifeReport.as_view(), name='url_life_report'),
]
