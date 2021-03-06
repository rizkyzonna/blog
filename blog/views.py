from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import Post
from .forms import PostForm


def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-pk')[:4]
	return render(request,'blog/post_list.html',{'posts':posts})

def bola (request):
	bola = Post.objects.filter(kategori='FootBall').order_by('-pk')[:4]
	return render(request, 'blog/bola.html', {'bola':bola})

def umum (request):
	umum = Post.objects.filter(kategori='umum').order_by('-pk')[:4]
	return render(request, 'blog/umum.html', {'umum':umum})
	
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new (request):
	if request.method == "POST":
		form	= PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author	= request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form':form})
# Create your views here.
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})