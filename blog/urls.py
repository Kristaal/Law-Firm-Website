from . import views
from django.urls import path


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('blog/', views.PostList.as_view(), name="blog"),
    path('about/', views.About.as_view(), name="about"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
