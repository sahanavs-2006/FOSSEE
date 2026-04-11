from django.conf.urls import url
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetConfirmView,
    PasswordResetDoneView, PasswordResetCompleteView,
    PasswordChangeView, PasswordChangeDoneView
)

urlpatterns = [
    url(r'^forgotpassword/$', PasswordResetView.as_view(),
        name="password_reset"),
    url(r'^password_reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
    url(r'^password_reset/mail_sent/$', PasswordResetDoneView.as_view(),
        name='password_reset_done'),
    url(r'^password_reset/complete/$', PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),
    url(r'^changepassword/$', PasswordChangeView.as_view(),
        name='password_change'),
    url(r'^password_change/done/$', PasswordChangeDoneView.as_view(),
        name='password_change_done'),
]
