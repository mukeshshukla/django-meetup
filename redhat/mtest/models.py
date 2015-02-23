from django.db import models

# Create your models here.

class Testing(models.Model):
	username = models.CharField(
		    max_length=200,
		    blank=False
		    )
	password = models.CharField(
			max_length = 200,
			blank = False
			)
	created_date = models.DateTimeField(
			auto_now_add = True
			)
