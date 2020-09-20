from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
import random
import string

# Create your models here.

def randomStrDig(strlen=4):
	"""
		Convenient methods to autogenerate string
	"""
	alpha_num 	= string.ascii_letters + string.digits

	return ''.join(random.choice(alpha_num) for i in range(strlen)).lower()

gen_str = randomStrDig()


class Post(models.Model):
	title 		= models.CharField(max_length=150)
	slug 		= models.SlugField(blank=True, null=True, unique=True)
	content 	= models.TextField()
	thumbnail 	= models.ImageField(upload_to='pic')
	published 	= models.BooleanField(default=True)
	pub_date	= models.DateTimeField('Date Published')
	timestamp	= models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.title


	class Meta:
		verbose_name = 'Blog Post'
		verbose_name_plural = 'Blog Posts'
		ordering = ['-pub_date']


@receiver(pre_save, sender=Post)
def auto_gen_slug(sender, instance, **kwargs):
	new_slug = "{}".format(instance.title)
	if instance.slug == "":
		instance.slug = slugify(new_slug+'-'+gen_str)