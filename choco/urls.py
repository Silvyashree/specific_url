from choco.views import *
from django.urls import path


app_name = 'dairy' 


urlpatterns = [
    
    path('dairy/',dairy , name ='dairy'),
    path('chocolate/',chocolate , name ='chocolate'),
]
