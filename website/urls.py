from django.urls import path
from django.contrib.auth import views as auth_views
from website.views import *

urlpatterns = [
    path('signup/', SignUp.as_view(), name="signup"),
    path('logout/', auth_views.LogoutView.as_view(next_page="/"), name='logout'),
    path('',index,name='home'),
    path('our_commands/',commands,name='our_commands'),
    path('works/', posts, name='works'),
    path('about_us/', about_us, name='about_us'),
    path('posts/<int:post_id>', post_details, name='post_detail'),
]
