from django.db import models

# Create your models here.
"""class Group(models.Model):
	name=models.CharField(max_length=255)
	"""

class Contact(models.Model):
	name= models.CharField(max_length=255)
	surname = models.CharField(max_length=255)
	description = models.TextField()
	#groups=models.ManyToManyField(Group)


class Adress(models.Model):
	city = models.CharField(max_length=255)
	street = models.CharField(max_length=255)
	number_of_house = models.IntegerField()
	contact=models.ForeignKey(Contact)


class Phone(models.Model):
	number=models.IntegerField()
	type_of_phone = models.CharField(max_length=64)
	contact=models.ForeignKey(Contact)


class Email(models.Model):
	email=models.TextField()
	type_of_email=models.CharField(max_length=64)
	contact=models.ForeignKey(Contact)
