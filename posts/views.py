from urllib.parse import quote_plus

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from django.contrib import messages
from .forms import PostForm

# Create your views here.

def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    print("awanti")
    if not request.user.is_authenticated():
        raise Http404

    if form.is_valid() == True:
        instance=form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request,"created successfully")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request,"not created at all")
    context = {"form": form}

    return render(request, "posts/post_create.html", context)




def post_list(request):
    queryset_list = Post.objects.all()  #.order_by("-timestamp")
    paginator = Paginator(queryset_list, 5)
    page_change_var = 'page'  #change=request
    page = request.GET.get(page_change_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list": queryset,
        "title": "LIST",
        "page_change_var":page_change_var
    }
    return render(request, 'posts/post_list.html', context)

def post_detail(request,slug=None):
    instance = get_object_or_404(Post,slug=slug)
    share_string = quote_plus(instance.content)
    context={
         "objs":instance,
         "title":instance.title,
         "share_string":share_string
    }
    return render(request,'posts/post_detail.html',context)


def post_update(request,slug=None):
    if not request.user.is_authenticated():
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid() == True:
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"Item Saved",)
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "objs": instance,
        "title": instance.title,
        "form": form
    }
    return render(request, "posts/post_create.html", context)


def post_delete(request, slug=None):
    if not request.user.is_authenticated():
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    return redirect("posts:list")


