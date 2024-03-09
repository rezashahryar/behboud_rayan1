from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(_('نام'), max_length=100)

    class Meta:
        verbose_name = _('دسته بندی')
        verbose_name_plural = _('دسته بندی ها')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(_('نام'), max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('بر چسب')
        verbose_name_plural = _('بر چسب ها')


class PostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=True, published_date__lte=timezone.now())


class Post(models.Model):
    title = models.CharField(_('عنوان'), max_length=255)
    description = HTMLField(verbose_name=_('توضیحات'))
    image = models.ImageField(_('عکس'), upload_to='post/image/%Y/%m/%d/', default='04.jpg')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts', verbose_name=_('دسته بندی'))
    tag = models.ManyToManyField(Tag, related_name='posts', blank=True, verbose_name=_('بر چسب'))
    slug = models.SlugField(_('مسیر یو ار ال'), null=True, blank=True, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts', null=True, blank=True, verbose_name=_('نویسنده'))

    published_date = models.DateTimeField(_('تاریخ انتشار'), null=True, blank=True)
    status = models.BooleanField(default=True)

    counted_views = models.IntegerField(_('تعداد بازدید'), default=0)

    datetime_created = models.DateTimeField(_('datetime_created'), auto_now_add=True)
    datetime_updated = models.DateTimeField(_('datetime_updated'), auto_now=True)

    objects = models.Manager()
    published = PostManager()

    class Meta:
        ordering = ('-published_date',)
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail_view', kwargs={'slug': self.slug})

    def get_category_objects(self):
        return reverse('blog:category_objects', kwargs={'cat_name': self.category})

