from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display: tuple = ("title", "slug", "description", "publish_datetime", "status",)
    list_filter: tuple = ("publish_datetime", "status",)
    search_fields: tuple = ("title", "description",)
    prepopulated_fields: dict = {"slug": ("title",)}
    ordering: list[str] = ["status", "-publish_datetime"]


# Register your models here.
admin.site.register(Article, ArticleAdmin)
