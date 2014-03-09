from django.forms import ModelForm
from blog.models import Comment
from captcha.fields import CaptchaField

class CommentForm(ModelForm):
	# Hide labels, so we can use translatable help text.
	auto_id=False
	# Captcha image and field.
	captcha = CaptchaField()

	class Meta:
		model = Comment
		exclude = ['article', 'author']
