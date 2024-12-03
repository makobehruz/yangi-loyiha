from django.shortcuts import render, redirect
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    ctx = {'posts': posts}
    return render(request, 'programs/1-dars.html', ctx)

def post_create(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    if name and description:
        Post.objects.create(
            name = name,
            description = description
        )
        return redirect('programs:post_list')
    return render(request, 'programs/2-dars.html')