from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404

from django import forms
from myapp.models import Post, PostForm
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.decorators import login_required




def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    context = {'posts': posts}

    # template = loader.get_template('list.html')
    # body = template.render({'posts': posts})
    # return HttpResponse(body, content_type="text/html")
    return render(request, 'list.html', context)


def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)

    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404

    context = {'post': post}
    return render(request, 'detail.html', context)


@login_required(login_url='/login')
def new_post(request):
    # if not request.user.is_authenticated:
    #     return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                model_instance = form.save(commit=False)
                model_instance.published_date = timezone.now()
                model_instance.author = request.user
                model_instance.save()
                return redirect('/')
        else:
            form = PostForm()
            return render(request, "add_post_form.html", {'form': form})



