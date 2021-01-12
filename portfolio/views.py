from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail

from . models import *
from . forms import *


def index(request):
    portfolio = Portfolio.objects.all()
    return render(request, 'portfolio/index.html', {'portfolio': portfolio})


def about(request):
    return render(request, 'portfolio/about.html')


def contact(request):
    return render(request, 'portfolio/contact.html')


def gallery(request):
    return render(request, 'portfolio/gallery.html')


def blog(request):
    return render(request, 'portfolio/blog.html')


def comment(request):
    return render(request, 'portfolio/comment.html')


def email(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            subject = 'Новое сообщение на сайте портфолио!'
            to_email = ['jumagylovaktilek566@gmail.com',]
            name = form.cleaned_data['name']
            mail = form.cleaned_data['mail']
            message = form.cleaned_data['message']
            msg = f'Имя: {name} \nПочта: {mail} \nСообщение: {message}'
            send_mail(subject, message, mail, to_email, fail_silently=False)
    return redirect('home')


def post_detail(request, post):
    post = get_object_or_404(Post, slug=post)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.post = post
        new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,'portfolio/comment.html',{'post': post,'comments': comments,'new_comment': new_comment,'comment_form': comment_form})








