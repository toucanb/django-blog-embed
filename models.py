from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy
from ckeditor.fields import RichTextField

class Category(models.Model):
	# Make sure there is no category or slug duplicates.
	name = models.CharField(max_length=30, unique=True)
	slug = models.SlugField(unique=True)

	# Fetch the category based on the slug.
	def get_absolute_url(self):
		return reverse('category_listing', kwargs={"requested_slug":self.slug})

	class Meta:
		verbose_name_plural = "categories"

	def __str__(self):
		return self.name

class Article(models.Model):
	# Make sure there is no title or slug duplicates.
	title = models.CharField(max_length=60, unique=True)
	slug = models.SlugField(unique=True)
	# Author as registered user selector.
	author = models.ForeignKey(User)
	# Autofill date.
	date = models.DateTimeField(auto_now_add=True)
	# Nice WYSIWYG editor from riklaunim's django-ckeditor-updated.
	body = RichTextField()
	# Multiple categories per articles.
	categories = models.ManyToManyField(Category, blank=True, null=True, through='CategoryToArticle')

	# Count the number of comments.
	def get_comment_count(self):
		return Comment.objects.filter(article=self).count()

	# Fetch the article based on the slug.
	def get_absolute_url(self):
		return reverse('article_detail', kwargs={"requested_slug":self.slug})

	# Ordering by date in admin.
	class Meta:
		ordering = ["-date"]

	def __str__(self):
		return self.title

class CategoryToArticle(models.Model):
	article = models.ForeignKey(Article)
	category = models.ForeignKey(Category)

	class Meta:
		verbose_name = "category"
		verbose_name_plural = "categories"

# Comments with captcha protection in forms.py.
class Comment(models.Model):
	article = models.ForeignKey(Article, related_name="comments", blank=True, null=True)
	# Autofill the date.
	date = models.DateTimeField(auto_now_add=True)
	# Identify bloggers separately to avoid imposters.
	author = models.ForeignKey(User, blank=True, null=True)
	# Optional name.
	name = models.CharField(max_length=30, blank=True, help_text=ugettext_lazy('Name (optional)'))
	# Optional email for Gravatar.
	email = models.EmailField(max_length=60, blank=True, help_text=ugettext_lazy('Gravatar email (optional)'))
	# Optional URL.
	website = models.URLField(max_length=120, blank=True, help_text=ugettext_lazy('Website (optional)'))
	# The actual comment.
	text = models.TextField(help_text=ugettext_lazy('Comment'))

	def __str__(self):
		return self.text[:60]
