from . import views
from django.urls import path,include

urlpatterns = {
    path('',views.home, name='home'),
    path('client_login',views.client_login, name='client_login'),
    path('client_lgn',views.client_lgn, name='client_login'),
    path('client_signup',views.client_signup, name='client_signup'),
    path('admin_login',views.admin_login, name='admin_login'),
    path('client_options',views.client_options, name='client_options'),
    path('admin_options',views.admin_options, name='admin_options'),
    path('view_books',views.view_books, name='view_books')
} 