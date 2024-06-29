from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    # path('login',views.login,name='login'),
    path('sendmail',views.sendMail ,name='sendmail'),
    path('registration',views.registration,name='registration'),
    path('otp-varification',views.varifyotp,name='otpvarify'),
    path('register',views.register,name='register'),
    path('uploadfile',views.uploadfile,name='uploadfile'),
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='index.html'), name='logout'),
    path('password-reset', views.resetPassword, name='passwordreset'),
    path('change-Password', views.changePassword, name='changePassword'),
    path('profile', login_required(views.profile), name='profile'),
    path('compose-mail', views.composeMail,name='composeMail'),
    path('delete-file/<int:id>',views.deletefile,name='delete'),
    path('update-file/<int:value>/<int:id>',views.updatefile,name='update')


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
