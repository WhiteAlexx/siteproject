from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from users import views

app_name = "users"

urlpatterns = [
    

    # path("pass-reset/", views.pass_reset_form, name="pass_reset"),
    # path("pass-reset/done/", views.pass_reset_done, name="pass_reset_done"),

    path("pass-reset/", auth_views.PasswordResetView.as_view(
        template_name="users/password_reset_form.html",
        from_email='webmaster@localhost',
        email_template_name="users/password_reset_email.html",
        success_url=reverse_lazy("users:pass_reset_done"),
        ),
        name="pass_reset"),
    path("pass-reset/done/", auth_views.PasswordResetDoneView.as_view(
        template_name="users/password_reset_done.html",
        ),
        name="pass_reset_done"),
    path("pass-reset-confirm/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(
        template_name="users/password_reset_confirm.html",
        success_url=reverse_lazy("users:pass_reset_complete"),
        ),
        name="pass_reset_confirm"),
    path("pass-reset-complete/", auth_views.PasswordResetCompleteView.as_view(
        template_name="users/password_reset_complete.html",
        ),
        name="pass_reset_complete"),

    path("login/", views.UserLoginView.as_view(), name="login"),
    path("registration/", views.UserRegistrationView.as_view(), name="registration"),
    path("profile/", views.UserProfileView.as_view(), name="profile"),
    path('users-cart/', views.UserCartView.as_view(), name='users_cart'),
    path("logout/", views.logout, name="logout"),

    path("payment/", views.payment, name="payment"),
]
