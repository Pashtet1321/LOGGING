from django.urls import path
from .views import PostList, PostDetail, PostCreate, ArticleCreate, ArticleUpdate, ArticleDelete, PostUpdate, \
   PostDelete, CategoryListView, subscribe
from django.views.decorators.cache import cache_page

urlpatterns = [

   path('', cache_page(60)(PostList.as_view()), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('create/', ArticleCreate.as_view(), name='article_create'),
   path('<int:pk>/update/', ArticleUpdate.as_view(), name='article_update'),
   path('<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe')
]


