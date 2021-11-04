from django.forms.fields import EmailField
from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import *
# Create your views here.

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blogf/post/list.html'

def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)
    posts = Post.published.all()
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)

    except PageNotAnInteger:
        #if page is not an integer deliver the first page 
        posts = paginator.page(1)
    except EmptyPage:
        #if page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request,
                    'blogf/post/list.html',
                    {'page': page,
                    'posts': posts})


def post_detail(request, year, month, day ,post):
    post = get_object_or_404(Post, slug=post,
                            status='published',
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)

    return render(request,
                'blogf/post/detail.html',
                {'post':post})

def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    if request.method == 'POST':
        # From was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            #Form fields passed validation
            cd = form.cleaned_data
            #..... send email
    else:
        form = EmailPostForm()
