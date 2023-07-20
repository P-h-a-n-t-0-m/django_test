from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("home/", Show_all_posts.as_view(), name="show_all_post"),
    path("create-new-post/", Newpost.as_view(), name="create_new_post"),
    path("update/<int:pk>/", UpdatePost.as_view(), name="update_post"),
    path("delete/<int:pk>/", DeletePost.as_view(), name="delete_post"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("password-reset/", PasswordResetView.as_view(template_name="blog/password_reset.html", success_url="/home/"),
         name="password_reset"),
    path("password-reset-confirm/<uidb64>/<token>/",
         PasswordResetConfirmView.as_view(template_name="blog/password_reset.html", success_url="/home/"),
         name="password_reset_confirm"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
