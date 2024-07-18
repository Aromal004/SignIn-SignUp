from django.urls import path
from . import views

urlpatterns=[
    path('',views.login,name='home'),
    path('register',views.register),
    path('logout',views.user_logout),
    path('get-data',views.getData),
    # path('printData',views.allData),
    path('addData',views.addData)
]