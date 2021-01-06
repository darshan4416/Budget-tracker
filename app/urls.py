from django.urls import path
from .views import home,signup,login,add_tracker,delete_tracker,signout

urlpatterns = [
    path('',home,name="home"),
    path('signup/',signup,name="signup"),
    path('login/',login,name="login"),
     path('logout/',signout,name="logout"),
    path('add-tracker/',add_tracker,name="add_tracker"),
    path('delete-tracker/<int:id>',delete_tracker,name="delete_tracker")
]
