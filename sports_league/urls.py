"""
URL configuration for sports_league project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rankings.views import TeamListView, MatchCreateView, MatchUpdateView, MatchDeleteView, process_csv
from django.contrib.auth import views as auth_views
from accounts.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TeamListView.as_view(), name='team_list'),
    path('match/create/', MatchCreateView.as_view(), name='match_create'),
    path('match/update/<int:pk>/', MatchUpdateView.as_view(), name='match_update'),
    path('match/delete/<int:pk>/', MatchDeleteView.as_view(), name='match_delete'),
    path('process-csv/', process_csv, name='process_csv'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', register, name='register'),

]

