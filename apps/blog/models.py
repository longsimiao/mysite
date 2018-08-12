from django.db import models
from mdeditor.fields import MDTextField


class Category(models.Model):
    category = models.CharField(max_length=50, unique=True, verbose_name='分类')
    description = models.CharField(max_length=200, verbose_name='描述')
    edit_time = models.DateTimeField(auto_now=True, verbose_name='编辑时间')

    def __str__(self):
        return self.category

    def save(self, *args, **kwargs):
        self.category = self.category.lower()
        super(Category, self).save(*args, **kwargs)


class Label(models.Model):
    label = models.CharField(max_length=50, unique=True, verbose_name='标签')
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


class Blog(models.Model):
    title = models.CharField(max_length=50, null=False, verbose_name='标题')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='作者')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    label = models.ManyToManyField(Label, verbose_name='标签')
    is_active = models.BooleanField(default=False, verbose_name='是否发表')
    body = MDTextField(verbose_name='正文')
    excerpt = models.CharField(max_length=200, blank=True)
    edit_time = models.DateTimeField(auto_now=True, verbose_name='编辑时间')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.excerpt = self.body[:51]
        super(Blog, self).save(*args, **kwargs)


# 评论功能
# class Comment(models.Model):
#     user = models.CharField(max_length=50, null=False, verbose_name='点评人')
#     time = models.TimeField(default=timezone.now(), verbose_name='评论时间')
#     is_active = models.BooleanField(default=False, verbose_name='是否审核通过')




