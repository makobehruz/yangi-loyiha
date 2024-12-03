from django.shortcuts import render, redirect
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    ctx = {'posts': posts}
    return render(request, 'cars/3-dars.html', ctx)

def post_create(request):
    name = request.POST.get('name')
    model = request.POST.get('model')
    year = request.POST.get('year')
    if name and model and year:
        Post.objects.create(
            name = name,
            model = model,
            year = year
        )
        return redirect('cars:post_list')
    return render(request, 'cars/4-dars.html')