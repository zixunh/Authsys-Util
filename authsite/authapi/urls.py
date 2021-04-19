from allauth.account.views import ConfirmEmailView
from django.conf.urls import url
from django.urls import include, path
from rest_auth.registration.views import RegisterView, VerifyEmailView
from rest_auth.views import LoginView, LogoutView, UserDetailsView

urlpatterns = [
    path('login/', LoginView.as_view(), name='account_login'),
    path('logout/', LogoutView.as_view(), name='account_logout'),
    path('registration/', RegisterView.as_view(), name='account_signup'),
    path('email/', UserDetailsView.as_view(), name='account_email'),
    path('rest-auth/', include('rest_auth.urls')), 
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
    path('rest-auth/verify-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
]
