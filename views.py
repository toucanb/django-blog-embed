from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse

from blog.models import Article, Comment, Category, CategoryToArticle
from blog.forms import CommentForm

def article_listing(request, requested_page=1):
	# Get all articles.
	articles = Article.objects.all().order_by('-date')

	# Configure pagination.
	pages = Paginator(articles, 10)

	# Get requested page.
	try:
		returned_page = pages.page(requested_page)
	except PageNotAnInteger:
		returned_page = pages.page(1)
	except EmptyPage:
		returned_page = pages.page(pages.num_pages)

	# Display all articles.
	return render(request, 'article_listing.html', {'articles': returned_page.object_list, 'page': returned_page})

def article_detail(request, requested_slug):
	# Get requested article.
	article = get_object_or_404(Article, slug=requested_slug)

	# Get comments from requested article.
	comments = Comment.objects.filter(article=article)

	# Configure comment form.
	form = CommentForm(request.POST or None)

	# If fields are filled and captcha is good.
	if form.is_valid():
		human = True
		comment = form.save(commit=False)
		comment.article = article
		comment.save()
		return redirect(request.path)

	# Display requested article.
	return render(request, 'article_detail.html', {'article': article, 'comments':comments, 'form': form})

def archive_index(request):
	# Get all articles.
	articles = Article.objects.all().order_by('-date')

	# Display all articles.
	return render(request, 'archive_index.html', {'articles': articles, 'archive': True})

def category_index(request):
	# Get all categories.
	categories = Category.objects.all().order_by('name')

	# Display all categories.
	return render(request, 'category_index.html', {'categories': categories})

def category_listing(request, requested_slug, requested_page=1):
	# Get articles from requested category.
	articles = Article.objects.all().order_by('-date')
	category_articles = []
	for article in articles:
		if article.categories.filter(slug=requested_slug):
			category_articles.append(article)

	# Configure pagination.
	pages = Paginator(category_articles, 10)

	# Get requested category
	category = Category.objects.filter(slug=requested_slug)[0]

	# Get requested page
	try:
		returned_page = pages.page(requested_page)
	except PageNotAnInteger:
		returned_page = pages.page(1)
	except EmptyPage:
		returned_page = pages.page(pages.num_pages)

	# Display all articles.
	return render(request, 'article_listing.html', { 'articles': returned_page.object_list, 'page': returned_page, 'category': category})

class LatestArticlesFeed(Feed):
	title = "Toucan Blanc"
	link = "/blog/"
	description = "Articles récemment publiés sur Toucan Blanc."

	def items(self):
		return Article.objects.order_by('-date')[:10]

	def item_title(self, item):
		return item.title

	def item_pubdate(self, item):
		return item.date

	def item_author_name(self, item):
		return item.author

	def item_author_email(self, item):
		return item.author.email

	def item_description(self, item):
		return item.body

	def item_categories(self, item):
		return item.categories.all()

	feed_copyright = 'Copyright (c) 2014, Toucan Blanc'
