from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView,PasswordResetDoneView,PasswordResetCompleteView
from .forms import LoginForm
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/eliminar/', views.post_delete, name='post_delete'),
    path('register',views.register),
    path('profile',views.userquery, name='profile'),
    path('post_profile',views.post_profile,name='post_profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path(r'^password_reset/$', PasswordResetView.as_view(), {'template_name': 'registration/password_reset_form.html'}),
    path('account/login/',views.LoginView.as_view(template_name="registration/login.html",authentication_form=LoginForm),name='login')
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)