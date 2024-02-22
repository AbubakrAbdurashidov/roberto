from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Tag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/blogs', blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(editable=False, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)


class BlogContent(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField()
    is_quote = models.BooleanField(default=False)


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='parent')
    top_level_comment = models.IntegerField(null=True, blank=True)

    @property
    def children(instance, *args, **kwargs):
        if not instance.top_level_comment:
            child = Comment.objects.filter(top_level_comment=instance.id).order_by('-id')
            return child
        else:
            return None

    def __str__(self):
        return self.blog


def comment_pre_save(sender, instance, *args, **kwargs):
    if instance.parent_comment:
        if instance.parent_comment.top_level_comment:
            instance.top_level_comment = instance.parent_comment.top_level_comment
        else:
            instance.top_level_comment = instance.parent_comment.id


def article_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title + "-" + str(timezone.now().date()))


pre_save.connect(article_pre_save, sender=Blog)
pre_save.connect(comment_pre_save, sender=Comment)
