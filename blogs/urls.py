from django.urls import path

from .views import blog, dashboard, feed, discover

urlpatterns = [
    path('', blog.home, name='home'),
    path('accounts/delete/', dashboard.delete_user, name='user_delete'),
    path('dashboard/', dashboard.dashboard, name='dashboard'),
    path('dashboard/domain/', dashboard.domain_edit, name='domain'),
    path('dashboard/posts/', dashboard.posts_edit, name='post'),
    path('dashboard/posts/new/', dashboard.post_new, name='post_new'),
    path('dashboard/posts/<pk>/', dashboard.post_edit, name='post_edit'),
    path('dashboard/posts/<pk>/delete/', dashboard.PostDelete.as_view(),
         name='post_delete'),
    path('discover/', discover.discover, name='discover'),

    path('blog/', blog.posts, name='posts'),
    path('hit/<pk>/', blog.post_hit, name='post_hit'),
    path("feed/", feed.feed, name="post_feed"),
    path('<slug>/', blog.post, name='post'),
]
