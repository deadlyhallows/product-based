from django.http import HttpResponse ,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from .models import Post
from django.contrib import messages
from .forms import PostForm

# Create your views here.
def post_create(request):
    form = PostForm(request.POST or None)

    if form.is_valid()==True:
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,"created successfully")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request,"not created")
    context = {"form": form}

    return render(request,"post_create.html",context)


def post_list(request):
    queryset_list = Post.objects.all()#.order_by("-timestamp")
    paginator = Paginator(queryset_list, 5)
    page_change_var = 'page' #change=request
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
    return render(request, 'post_list.html', context)

def post_detail(request,id=None):
    instance = get_object_or_404(Post,id=id)
    context={
         "objs":instance,
         "title":instance.title
    }
    return render(request,'post_detail.html',context)


def post_update(request,id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None,instance=instance)

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
    return render(request, "post_create.html", context)


def post_delete(request,id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    return  redirect("posts:list")

