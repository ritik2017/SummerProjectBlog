from django.shortcuts import render, redirect
from Blog.models import Blog

# function based views


def blogs(request):
    '''
    get list of all blogs
    '''
    blogs = Blog.objects.all()
    return render(request, 'blogs.html', {'blogs': blogs})

def blog_create(request):
    '''
    create a single blog.
    '''
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST['title']
            body = request.POST['body']
            blog = Blog.objects.create(title=title, body=body, created_by=request.user)
            return redirect('blog_view', blog.pk)
        return render(request, 'blog_create.html')
    return redirect('root')

def blog_view(request, pk):
    '''
        view a blog.
    '''
    blog = Blog.objects.get(pk=pk)
    return render(request, 'blog.html', {'blog': blog})
