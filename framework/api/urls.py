from django.urls import path

from . import views

urlpatterns = [
    path(
        "blog/create/", views.BlogPostListCreate.as_view(), name="blogpost-list-create"
    ),
    path(
        "blog/<int:pk>/", views.BlogPostRetrieveUpdateDestroy.as_view(), name="update"
    ),
    path("blog/list/", views.BlogPostList.as_view(), name="blogpost-list"),
    # ...
]
