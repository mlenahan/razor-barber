from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import BlogPost, Reply
from .forms import ReplyForm


def blog_overview(request):

    posts = BlogPost.objects.all()

    template = 'blog/blog_overview.html'
    context = {
        'posts': posts,
    }

    return render(request, template, context)


def blog_detail(request, blog_id):

    queryset = BlogPost.objects
    post = get_object_or_404(queryset, pk=blog_id)
    replies = post.blog_replies.all()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'Action not allowed')
            return redirect(reverse('home'))
        else:
            reply_form = ReplyForm(request.POST)
            if reply_form.is_valid():
                reply_form.instance.creator = request.user
                reply = reply_form.save(commit=False)
                reply.post = post
                reply.save()
                messages.success(request, 'Reply successfully added!')
            else:
                messages.error(request, 'Reply not added!')

    form = ReplyForm()
    template = 'blog/blog_detail.html'
    context = {
        'post': post,
        'replies': replies,
        'form': form,
    }

    return render(request, template, context)


@login_required
def blog_reply_edit(request, reply_id):

    queryset = Reply.objects
    reply = get_object_or_404(queryset, pk=reply_id)
    post = reply.post
    replies = post.blog_replies.all()

    if request.user != reply.creator:
        messages.error(request, 'Action not allowed')
        return redirect(reverse('home'))

    if request.method == 'POST':
        reply_form = ReplyForm(request.POST, instance=reply)
        if reply_form.is_valid():
            reply_form.save()
            messages.success(request, 'Reply successfully amended!')
            return redirect(reverse('blog_detail', args=[post.id]))
        else:
            messages.error(request, 'Reply not amended!')

    messages.info(request, 'Editing reply')

    form = ReplyForm(instance=reply)
    template = 'blog/blog_reply_edit.html'
    context = {
        'post': post,
        'replies': replies,
        'form': form,
    }

    return render(request, template, context)


@login_required
def blog_reply_confirm_delete(request, reply_id):

    queryset = Reply.objects
    reply = get_object_or_404(queryset, pk=reply_id)
    post = reply.post

    if request.user != reply.creator:
        messages.error(request, 'Action not allowed')
        return redirect(reverse('home'))

    template = 'blog/blog_reply_confirm_delete.html'
    context = {
        'post': post,
        'reply': reply,
    }

    return render(request, template, context)


@login_required
def blog_reply_delete(request, reply_id):

    queryset = Reply.objects
    reply = get_object_or_404(queryset, pk=reply_id)
    post = reply.post

    if request.user != reply.creator:
        messages.error(request, 'Action not allowed')
        return redirect(reverse('home'))
    else:
        reply.delete()
        messages.success(request, 'Reply deleted!')
        return redirect(reverse('blog_detail', args=[post.id]))
