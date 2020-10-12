from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name='home'),
    path('loginPage/', views.loginPage,name='login'),
    path('register/', views.register,name='register'),
    path('logoutUser/', views.logoutUser,name='logout'),
    path('addExpense', views.addExpense,name='addExpense'),
    path('expenseReport', views.expenseReport,name='expenseReport'),
    path('profile', views.profile,name='profile'),
    path('viewProfile/<str:slug>', views.viewProfile,name='viewProfile'),

] 
 