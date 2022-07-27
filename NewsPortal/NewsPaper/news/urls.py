from django.urls import path

from .views import (
    NewsList, NewsDetail, SearchList, create_post, PostEdit, PostDelete,
)


urlpatterns = [
    path('', NewsList.as_view(), name='post_list'),
    path('<int:pk>', NewsDetail.as_view(), name='post_detail'),
    path('search/', SearchList.as_view(), name='post_search'),
    path('news/create/', create_post, name='news_create'),
    path('post/create/', create_post, name='post_create'),
    path('<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]
