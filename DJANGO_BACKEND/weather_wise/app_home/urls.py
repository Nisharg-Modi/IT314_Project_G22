from django.urls import path
from app_home import views
urlpatterns = [
    path('',views.home_view,name="home_view"),
    path('about/',views.about_view,name="about_view"),
    path('login/',views.login_view,name="login_view"),
    path('logout/',views.logout_view,name="logout_view"),
    path('signup/',views.signup_view,name="signup_view"),
    path('predict/',views.predict_view,name="predict_view"),
    path('profile/',views.profile_view,name="profile_view"),
    path('profile/edit/', views.profile_edit_view, name='profile_edit_view'),
]
