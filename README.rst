Django Blog Embed
=================

Django Blog Embed is a minimalist blog application designed to be integrated into an existing website without getting in the way!

Features
--------

* Up to date with Django 1.6 and Python 3.
* Uses h3, h4 and h5 tags to adapt to your base stylesheet.
* WYSIWYG editing for blog articles thanks to CKEditor.
* Comment system that supports anonymous, optional name, and registered users.
* Gravatar support through optional email field.
* Basic spam prevention with simple captcha.
* Categorized browsing and multiple categories per articles.
* Minimalist archive will display all posts in a list.
* RSS 2.0 feed.

Requirements
------------

* Django 1.6+
* Python 3 with Pillow 2.2+
* Django-CKEditor-Updated
* Django-Gravatar2
* Django-Simple-Captcha

Installation
------------

This is not a stand-alone blog, it's best to add it to an existing development project::

	cd /django/project/
	git clone https://github.com/toucanb/django-blog-embed.git blog

Install requirements if it's not already done::

	pip install -r requirements.txt

A few changes to the project ``settings.py`` are necessary::

	INSTALLED_APPS = (
		#...
		'ckeditor',
		'captcha',
		'django_gravatar',
		'blog',
	)
	
	USE_I18N = True
	
	STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
	STATIC_URL = '/static/'
	MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
	MEDIA_URL = '/media/'
	
	CKEDITOR_UPLOAD_PATH = 'uploads/'
	CKEDITOR_SLUGIFY_FILENAME = True
	CKEDITOR_RESTRICT_BY_USER = True
	CKEDITOR_IMAGE_BACKEND = 'pillow'
	CKEDITOR_CONFIGS = {
		'default': {
			'format_tags' : 'h4;pre',
			'toolbar_Blog': [
				['Undo', 'Redo'],
				['Format',],
				['Bold', 'Italic', 'Underline', 'Strike', 'TextColor', 'SpecialChar'],
				['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
				['Image', 'Youtube', 'Table',],
				['Source'],
			],
			'toolbar': 'Blog',
			'width': 750, # Make this the width of your content container.
			'height': 500,
		},
	}

Configure the project ``urls.py``::

	urlpatterns = patterns('',
		#...
		url(r'^blog/', include('blog.urls')),
		url(r'^admin/', include(admin.site.urls)),
		url(r'^ckeditor/', include('ckeditor.urls')),
		url(r'^captcha/', include('captcha.urls')),
	)

Configure the feed at the bottom of the blog ``views.py`` file, and you're done!

Changelog
---------

* 2014-03-08
	- Initial release.

Licence
-------

This project is licensed under the terms of the BSD 3-Clause License.

A copy of the licence is included.
