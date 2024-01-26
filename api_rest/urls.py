from django.urls import path
from . import views

urlpatterns = [
        path('all', views.get_users, name='get_all_users'),
        path('user/<str:nick>', views.get_by_nick),
        path('add/', views.add_user),
        path('update/',views.upt_user),
        path('delete/', views.del_user)
]