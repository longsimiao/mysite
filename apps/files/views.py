# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from apps.blog.models import Blog
from .models import PersonalDescription, SpecialArticle, Label


def index(request):
    blogs = Blog.objects.filter(is_active=True).order_by('-edit_time')[:5]
    my_description = PersonalDescription.objects.filter(is_active=True).\
        filter(type='Desc').order_by('-edit_time')
    my_experience = PersonalDescription.objects.filter(is_active=True).\
        filter(type='Exp').order_by('-edit_time')
    interest = PersonalDescription.objects.filter(is_active=True).\
        filter(type='Interest').order_by('-edit_time')
    special = SpecialArticle.objects.filter(is_active=True).\
        order_by('-edit_time')
    return render(request, 'base.html', {
        'blogs': blogs, 'description': my_description,
        'experience': my_experience, 'interest': interest,
        'special': special})


def login(request):
    slug = 'login'
    if request.user.is_authenticated:
        next_url = request.GET.get('next', '/')
        return HttpResponseRedirect(next_url)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.GET.get('next', '/')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            response = HttpResponseRedirect(next_url)
            response.set_cookie('username', username, 3600)
            return response
    return render(request, 'auth/login.html', {'slug': slug})


@login_required(login_url='/login')
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def special_lists(request):
    slug = 'labels'
    labels = Label.objects.all()
    return render(request, 'files/lists.html', {
        'slug': slug, 'labels': labels})


def special_labels(request, ctg):
    slug = ctg.capitalize()
    labels = Label.objects.all()
    label = Label.objects.filter(label=ctg.capitalize()).values('id', 'label')
    articles = SpecialArticle.objects.filter(is_active=True).\
        filter(label=label[0].get('id')).order_by('-edit_time')
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request, 'files/labels.html', {
        'slug': slug, 'articles': articles, 'labels': labels})


def show_special_detail(request, ctg):
    slug = ctg
    sid = request.GET.get('sid')
    labels = Label.objects.all()
    label = Label.objects.filter(label=ctg).values('id', 'label')
    spcs = SpecialArticle.objects.filter(is_active=True).\
        filter(label=label[0].get('id')).order_by('-edit_time')
    spc = SpecialArticle.objects.filter(is_active=True).filter(id=sid)
    return render(request, 'files/article.html', {
        'slug': slug, 'spc': spc, 'spcs': spcs, 'labels': labels})


def handler404(request, exception):
    context = RequestContext(request)
    err_code = 404
    response = render_to_response('404.html', {"code":err_code}, context)
    response.status_code = 404
    return response

