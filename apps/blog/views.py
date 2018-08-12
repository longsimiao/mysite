# -*- coding: utf-8 -*-

import markdown
# import markdown2
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from .models import Blog, Category


def lists(request):
    slug = 'ctgs'
    ctgs = Category.objects.all()
    return render(request, 'blog/lists.html', {'ctgs': ctgs, 'slug': slug})


def category(request, ctg='python'):
    slug = ctg.lower()
    ctgs = Category.objects.all()
    ctg = Category.objects.filter(category=slug).values('id', 'category')
    blogs = Blog.objects.filter(is_active=True). \
        filter(category=ctg[0].get('id')).order_by('-edit_time')
    paginator = Paginator(blogs, 5)
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    return render(request, 'blog/category.html', {
        'blogs': blogs, 'slug': slug, 'ctgs': ctgs})


def detail(request, ctg='python'):
    slug = ctg
    bid = request.GET.get('bid')
    ctgs = Category.objects.all()
    ctg = Category.objects.filter(category=ctg.lower()).values('id',
                                                               'category')
    blogs = Blog.objects.filter(is_active=True). \
        filter(category=ctg[0].get('id')).order_by('-edit_time')
    blog = Blog.objects.filter(is_active=True).get(id=bid)
    blog.body = markdown.markdown(blog.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    # blog.body = markdown2.markdown(blog.body, extras=[
    #     "code-friendly",
    #     "fenced-code-blocks",
    #     "footnotes",
    #     "header-ids",
    # ])
    return render(request, 'blog/blog.html', {
        'blog': blog, 'slug': slug, 'ctgs': ctgs, 'blogs': blogs, 'bid': bid})
