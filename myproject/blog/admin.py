from django.contrib import admin
from .models import Article, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display: tuple = ("position", "title", "slug", "status",)
    list_filter: tuple = (["status"])
    search_fields: tuple = ("title", "slug",)
    prepopulated_fields: dict = {"slug": ("title",)}


# Register your models here.
admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display: tuple = ("title", "slug", "description", "publish_datetime", "status", "_category_to_str",)
    list_filter: tuple = ("publish_datetime", "status",)
    search_fields: tuple = ("title", "description",)
    prepopulated_fields: dict = {"slug": ("title",)}
    ordering: list[str] = ["status", "-publish_datetime"]

    def _category_to_str(self, obj: Article) -> str:
        return "، ".join([category.title for category in (obj.category.all())])
    _category_to_str.short_description: str = "دسته بندی"


# Register your models here.
admin.site.register(Article, ArticleAdmin)
