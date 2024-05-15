from django.urls import path
from .views import index,profile,donate_faq
from django.contrib.auth import views
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns =[
    path('', index, name='index'),
    path('profile/', profile, name='profile'),
    path('details/', views.details, name='details'),
    path('profile_details/', views.profile_details, name='profile_details'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('donate/', views.donate, name="donate"),
    path('donate_faq/', views.donate_faq, name="donate_faq"),
    path('classroom/', views.classroom, name="classroom"),
    path('jobs/', views.jobs, name="jobs"),
    path('faqs/', views.faqs, name="faqs"),
    path('terms/', views.terms, name="terms"),
    path('ways_to_give/', views.terms, name="terms"),
    path('customer_support/', views.ways_to_give, name="ways_to_give"),
    path('create/', views.create_post, name='create_post'),
    # path('update_profile_picture/', views.update_profile_picture, name='update_profile_picture'),
]
