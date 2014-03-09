from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('blog.views',
	# ex: http://www.exemple.com/blog/
	url(r'^$', 'article_listing', name='article_listing'),
	# ex: http://www.exemple.com/blog/2/
	url(r'^(?P<requested_page>\d+)/?$', 'article_listing', name='article_listing'),
	# ex: http://www.exemple.com/blog/article/the-article-slug/
	url(r'^article/(?P<requested_slug>[-\w]+)/?$', 'article_detail', name='article_detail'),
	# ex: http://www.exemple.com/blog/archive/
	url(r'^archive/$', 'archive_index', name='archive_index'),
	# ex: http://www.exemple.com/blog/category/
	url(r'^category/$', 'category_index', name='category_index'),
	# ex: http://www.exemple.com/blog/category/the-category-slug/
	url(r'^category/(?P<requested_slug>[-\w]+)/?$', 'category_listing', name='category_listing'),
	# ex: http://www.exemple.com/blog/category/the-category-slug/2/
	url(r'^category/(?P<requested_slug>[-\w]+)/(?P<requested_page>\d+)/?$', 'category_listing', name='category_listing'),
	# ex: http://www.exemple.com/blog/feed/
	url(r'^feed/$', views.LatestArticlesFeed(), name='feed'),
)
