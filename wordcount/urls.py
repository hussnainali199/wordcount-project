
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Homepage, name='home'),
    path('count/',views.countfunction, name='COUNTIT'), #'count/ is the urlname'
    path('about/',views.aboutpage, name='about')

]
