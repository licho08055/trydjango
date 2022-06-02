from django.urls import path
from .views import (
    ArticleList,
    ArticleDetail,
    ArticleCreate,
    ArticleUpdate,
    ArticleDelete
)

app_name = 'articles'
urlpatterns = [
    path('', ArticleList.as_view(), name='article-list'),
    path('<int:id>/', ArticleDetail.as_view(), name='detail'),
    path('create/', ArticleCreate.as_view(), name='create' ),
    path('<int:id>/update/', ArticleUpdate.as_view(), name='update'),
    path('<int:id>/delete/', ArticleDelete.as_view(), name='delete'),
]