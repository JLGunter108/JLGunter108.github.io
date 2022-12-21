from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Comment, Post, Album
from .forms import CommentForm, CreateAlbumForm, EditAlbumForm, EditPostForm, PostForm
from django.urls import reverse_lazy, reverse
import os

def index(request):
    return render(request, 'index.html')

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView, CreateView):
    model = Post
    form_class = CommentForm
    template_name = 'post_details.html'

def RemoveCommentView(request, pk):
    comment = get_object_or_404(Comment, id=request.POST.get('comment_id'))
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    comment.delete()
    return HttpResponseRedirect(f'/post/{post.id}')

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(f'/post/{post.id}')

def removeLikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.remove(request.user)
    return HttpResponseRedirect(f'/post/{post.id}')

def CommentLikeView(request, pk):
    comment = get_object_or_404(Comment, id=request.POST.get('comment_id'))
    comment.likes.add(request.user)
    return HttpResponseRedirect(f'/post/{comment.post.id}')

def removeCommentLikeView(request, pk):
    comment = get_object_or_404(Comment, id=request.POST.get('comment_id'))
    comment.likes.remove(request.user)
    return HttpResponseRedirect(f'/post/{comment.post.id}')

class UploadView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'upload.html'

class EditPostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'edit_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class ViewAlbumCreate(CreateView):
    model = Album
    form_class = CreateAlbumForm
    template_name = 'album_create.html'

class AlbumDetailsView(DetailView):
    model = Album
    template_name = 'album.html'

class AlbumEditView(UpdateView):
    model = Album
    form_class = EditAlbumForm
    template_name = 'edit_album.html'

class AlbumDeleteView(DeleteView):
    model = Album
    template_name = 'delete_album.html'
    success_url = reverse_lazy('home')

def AlbumAddView(request, pk):
    album = get_object_or_404(Album, id=request.POST.get('album_id'))
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    album.posts.add(post)
    return HttpResponseRedirect(f'/album/{album.id}/edit')

def AlbumRemoveView(request, pk):
    album = get_object_or_404(Album, id=request.POST.get('album_id'))
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    album.posts.remove(post)
    return HttpResponseRedirect(f'/album/{album.id}/edit')