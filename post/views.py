from django.shortcuts import get_object_or_404, render, redirect

from .models import Post, Comment

def bloghome(request):
    posts = Post.objects.all()

    return render(request, 'post/bloghome.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        comment = request.POST.get('comment', '')

        if name and comment:
            Comment.objects.create(
                post = post, name = name, comment = comment
            )
        return redirect('post_detail', slug = post.slug)

    return render(request, 'post/detail.html', {'post': post})