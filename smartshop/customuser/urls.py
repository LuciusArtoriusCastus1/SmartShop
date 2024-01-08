from django.urls import path

from customuser.views import SignUpUserView, log_out, SignInUserView, UpgradeToSeller

urlpatterns = [
    path('signup/', SignUpUserView.as_view(), name='signup'),
    path('logout/', log_out, name='logout'),
    path('login/', SignInUserView.as_view(), name='login'),
    path('upgradeuser/<str:pk>/', UpgradeToSeller.as_view(), name='upgradeuser')
]
