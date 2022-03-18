from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from blogs.forms import BlogPostForm
from .models import BlogPost

# Create your views here.
def index(request):
    """The home page for Blogs."""
    blog_posts = BlogPost.objects.order_by('-date_added')
    context = {
        'blog_posts': blog_posts,
    }
    return render(request, 'blogs/index.html', context)

@login_required
def blogs(request):
    """The home page for Blogs."""
    # print(request.user)
    blog_posts = BlogPost.objects.filter(owner=request.user).order_by('-date_added')
    context = {
        'blog_posts': blog_posts,
    }
    return render(request, 'blogs/blogs.html', context)
@login_required
def new_post(request):
    """Add a new blog post."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogPostForm()
    else:
        # POST data submitted; process data.
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_post = form .save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:blogs')
     # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    """Edit a blog post."""
    post = BlogPost.objects.get(id=post_id)
    print(post)
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = BlogPostForm(instance=post)
    else:
        # POST data submitted; process data.
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogs')
    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)