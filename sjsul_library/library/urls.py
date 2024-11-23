from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('register/', views.register, name='register'),  # Register page
    path('login/', views.login_user, name='login'),  # Login page
    path('logout/', views.logout_user, name='logout'),  # Logout page
    path('signup/', views.signup, name='signup'), # Signup page
    path('member-dashboard/', views.member_dashboard, name='member_dashboard'), # Member dashbaord
    path('librarian-dashboard/', views.librarian_dashboard, name='librarian_dashboard'),  # Librarian dashboard
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),  # Admin dashboard
    path('unauthorized/', views.unauthorized, name='unauthorized'), # Unauthorized page
]
