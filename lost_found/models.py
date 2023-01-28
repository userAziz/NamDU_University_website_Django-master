from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class lost_found(models.Model):
	item_name = models.CharField(max_length=100)
	slug_path = models.SlugField(unique="True")
	item_description = models.TextField()
	date = models.DateTimeField(auto_now_add = True)
	image = models.ImageField(default='default.png',upload_to='post_image',blank=True)
	author = models.ForeignKey(User, default=None, on_delete = models.DO_NOTHING, null=True)

	def __str__(self):
		return self.item_name

	def snippet(self):
		return self.item_description[:500]