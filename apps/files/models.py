# -*- coding: utf-8

from django.db import models
from mdeditor.fields import MDTextField


class PersonalDescription(models.Model):
    choices = (
        ('Desc', '我的简介'),
        ('Exp', '我的经历'),
        ('Interest', '兴趣爱好'),
    )
    title = models.CharField(max_length=20, unique=True, verbose_name='标题')
    is_active = models.BooleanField(verbose_name='是否发布')
    type = models.CharField(max_length=20, choices=choices, verbose_name='类别', default='Desc')
    description = models.TextField(verbose_name='个人描述')
    edit_time = models.DateTimeField(auto_now=True, verbose_name='编辑时间')


class Label(models.Model):
    label = models.CharField(max_length=50, unique=True, verbose_name='系列')
    description = models.CharField(max_length=200, verbose_name='描述')
    edit_time = models.DateTimeField(auto_now=True, verbose_name='编辑时间')

    def __str__(self):
        return self.label

    def save(self, *args, **kwargs):
        self.label = self.label.lower().capitalize()
        super(Label, self).save(*args, **kwargs)


class Author(models.Model):
    author = models.CharField(max_length=50, verbose_name='作者')
    edit_time = models.DateTimeField(auto_now=True, verbose_name='编辑时间')

    def __str__(self):
        return self.author


class SpecialArticle(models.Model):
    title = models.CharField(max_length=30, verbose_name='标题')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='作者')
    label = models.ForeignKey(Label, on_delete=models.CASCADE, verbose_name='系列')
    is_active = models.BooleanField(default=False, verbose_name='是否发表')
    body = MDTextField(verbose_name='正文')
    excerpt = models.CharField(max_length=200, blank=True)
    edit_time = models.DateTimeField(auto_now=True, verbose_name='编辑时间')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.excerpt = self.body[:51]
        super(SpecialArticle, self).save(*args, **kwargs)

