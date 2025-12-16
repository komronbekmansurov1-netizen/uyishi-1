from django.contrib import admin
from .models import Store, Book, Author
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "surname"]
    search_fields = ["name", "surname"]

admin.site.register(Author, AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ["name", "author", "cover", "price", "in_stock"]
    search_fields = ["name", "author", "janri"]
    list_filter = ["janri"]

admin.site.register(Book, BookAdmin)

class StoreAdmin(admin.ModelAdmin):
    list_display = ["name", "total_of_sold", "shop_assistant"]
    search_fields = ["name"]

admin.site.register(Store, StoreAdmin)