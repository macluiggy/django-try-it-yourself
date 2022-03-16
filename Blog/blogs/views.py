from django.shortcuts import render, redirect

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

def new_post(request):
    """Add a new blog post."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogPostForm()
    else:
        # POST data submitted; process data.
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_post = form .save()
            return redirect('blogs:index')
     # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

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
            return redirect('blogs:index')
    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)