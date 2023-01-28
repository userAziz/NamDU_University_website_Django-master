from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
	article_title = models.CharField(max_length=100)
	slug = models.SlugField(unique="True")
	body = models.TextField()
	date = models.DateTimeField(auto_now_add = True)
	thumb = models.ImageField(default='default.png',upload_to='post_image',blank=True)
	author = models.ForeignKey(User, default=None, on_delete = models.DO_NOTHING, null=True)

	def __str__(self):
		return self.article_title

	def snippet(self):
		return self.body[:370]+ " ..."