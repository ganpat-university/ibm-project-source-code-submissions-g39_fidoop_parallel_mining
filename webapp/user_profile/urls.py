from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^accounts/profile/$', views.UserProfileView.as_view(), name="profile"),
    url(r'^accounts/status/$', views.UserStatusView.as_view(), name="status"),
    # dashboard url is added here
    url(r'^dashboard/', views.DashboardView.as_view(), name="dashboard"),

    url(r'^accounts/upload/$', views.UserUploadView.as_view(), name="upload"),
    url(r'^accounts/success/$', views.UserUploadSuccessView.as_view(), name="success"),
    
]