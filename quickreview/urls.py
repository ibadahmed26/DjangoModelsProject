
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('page/', views.page, name='page'),
    path('post/', views.post, name='post'),
    path('song/', views.song, name='song'),
    path('user/', views.user, name='user'),
]
