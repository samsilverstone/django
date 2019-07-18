from django.conf.urls import url
from django.urls import path
from knox import views as knox_views


from geoapi.api import *

urlpatterns=[
    path('district/',DistrictView.as_view()),
    path('district/<int:pk>/',DistrictDetailView.as_view()),
    url(r'auth/register/$',RegistrationAPI.as_view()),
    url(r'auth/login/$',LoginAPI.as_view()),
    url(r'auth/logout/$',knox_views.LogoutView.as_view(),name='knox_logout'),
]
# urlpatterns = format_suffix_patterns(urlpatterns)
