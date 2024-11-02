from django.shortcuts import redirect, render
from blogs.models import Post
from .forms import PostForm

def frontpage(request):
    posts = Post.objects.all()
    return render(request,'core/frontpage.html',{'posts':posts})

def about(request):
    return render(request,'core/about.html')

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('frontpage')  # Redirect to homepage or list of posts
    else:
        form = PostForm()
    return render(request, 'core/create_post.html', {'form': form})