"""
URL configuration for my_project project.

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
from django.urls import path
# from .views import users , get_update_or_delete
#from .better_views import UserListCreateAPIView,UserRetrieveUpdateDestroyAPIView
from .custom_apiViews import UserListCreateApiView
# urlpatterns = [
#     path('users/', users),
#     path('users/<id>', get_update_or_delete),
#     path('admin/', admin.site.urls),
# ]
# Better views

# urlpatterns = [
#     path('users/', UserListCreateAPIView.as_view()),
#     path('users/<id>', UserRetrieveUpdateDestroyAPIView.as_view()),
#     path('admin/', admin.site.urls),
# ]

#custom API views
urlpatterns = [
    path('users/', UserListCreateApiView.as_view()),
    path('admin/', admin.site.urls),
]