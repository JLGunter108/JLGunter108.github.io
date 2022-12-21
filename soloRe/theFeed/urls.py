from django.urls import path
from . import views
from .views import AlbumAddView, AlbumDeleteView, AlbumDetailsView, AlbumEditView, EditPostView, HomeView, PostDetailView, UploadView, DeletePostView, LikeView, CommentLikeView, removeLikeView, removeCommentLikeView, ViewAlbumCreate, AlbumRemoveView, RemoveCommentView

urlpatterns = [
    path('', views.index, name='index'),
    path('home', HomeView.as_view(), name='home'),
    path('post/<pk>', PostDetailView.as_view(), name='post-details'),
    path('upload/', UploadView.as_view(), name='upload'),
    path('post/<int:pk>/edit', EditPostView.as_view(), name='edit_post'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('like/<int:pk>', LikeView, name='like'),
    path('like/<int:pk>/remove', removeLikeView, name='like_remove'),
    path('like/comment/<int:pk>', CommentLikeView, name='comment_like'),
    path('like/comment/<int:pk>/remove', removeCommentLikeView, name='comment_like_remove'),
    path('album/<int:pk>', AlbumDetailsView.as_view(), name='album'),
    path('album/<int:pk>/delete', AlbumDeleteView.as_view(), name='album_delete'),
    path('create/album', ViewAlbumCreate.as_view() , name='albumCreate'),
    path('album/<int:pk>/edit', AlbumEditView.as_view(), name='edit_album'),
    path('album/<int:pk>/add', AlbumAddView, name='add_to_album'),
    path('album/<int:pk>/remove', AlbumRemoveView, name='remove_from_album'),
    path('comment/<int:pk>/delete', RemoveCommentView, name='remove_comment'),
]
