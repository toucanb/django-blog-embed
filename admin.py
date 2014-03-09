from django.contrib import admin
from django.contrib.auth.models import User

from blog.models import Category, CategoryToArticle, Comment, Article

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ('name',)

	prepopulated_fields = {'slug': ('name',)}
	fieldsets = [
		(None, {'fields': ('name', 'slug',)}),
	]

class CategoryToArticleInline(admin.TabularInline):
	model = CategoryToArticle
	extra = 3

class CommentAdmin(admin.ModelAdmin):
	list_display = ('article', 'author', 'name', 'email', 'website', 'text',)
	search_fields = ('text',)

	exclude = ('author', 'name', 'email')
	fieldsets = [
		(None, {'fields': ('article', 'website', 'text',)}),
	]

	# Autofill author and email from user.
	def save_model(self, request, obj, form, change):
		obj.author = request.user
		obj.email = request.user.email
		obj.save()

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'date')
	search_fields = ('title',)

	prepopulated_fields = {'slug': ('title',)}
	exclude = ('author',)
	inlines = [CategoryToArticleInline]

	# Autofill author from user.
	def save_model(self, request, obj, form, change):
		obj.author = request.user
		obj.save()

admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Article, ArticleAdmin)
