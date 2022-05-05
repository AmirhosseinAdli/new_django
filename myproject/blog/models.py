from datetime import datetime

from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس دسته بندی")
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")

    class Meta:
        verbose_name: str = "دسته بندی"
        verbose_name_plural: str = "دسته بندی ها"
        ordering: list[str] = ['position']

    def __str__(self):
        return self.title


# Create your models here.
class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published')
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ManyToManyField(Category, verbose_name="دسته بندی")
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="images")
    publish_datetime = models.DateTimeField(default=datetime.utcnow())
    creation_datetime = models.DateTimeField(auto_now_add=True)
    last_update_datetime = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title
