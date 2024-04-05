from django.contrib import admin
from .models import Book, Author, BookingBook, Comments
from import_export.admin import ImportExportModelAdmin

@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'birth_date')
    list_display_links = ('id', 'first_name', 'last_name', 'birth_date')
    search_fields = ('first_name', 'last_name', )
    ordering = ('id', 'first_name', )


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'description', 'price', 'count', 'author', 'create_date')
    list_display_links = ('id', 'title', 'description', 'price', 'count', 'author', 'create_date')
    search_fields = ('id', 'title', )
    ordering = ('id', 'title', )
    autocomplete_fields = ['author']


@admin.register(BookingBook)
class BookingBookAdmin(ImportExportModelAdmin):
    list_display = ('id', 'student', 'book', 'take_date', 'return_date')

    def student(self, obj):
        return obj.count()
    def book(self):
        return self.count()


@admin.register(Comments)
class CommentsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'text', 'student')

