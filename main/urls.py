from django.urls import path
from .views import *

app_name = 'main'
urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', by_rubric, name='by_rubric'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('accounts/register/activate/<str:sign>/', user_activate,
         name='register_activate'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/password/change/', BBPasswordChangeView.as_view(), name='password_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/profile/detail/<int:pk>/', profile_detail, name='profile_detail'),
    path('accounts/profile/add/', profile_bb_add, name='profile_bb_add'),
    path('accounts/profile/change/<int:pk>/', profile_bb_change, name='profile_bb_change'),
    path('accounts/profile/delete/<int:pk>/', profile_bb_delete, name='profile_bb_delete'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/profile/delete/', DeleteUserView.as_view(), name='profile_delete'),
    path('<str:page>/', other_page, name='other'),
]
