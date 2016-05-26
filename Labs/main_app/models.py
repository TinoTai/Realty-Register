from django.db import models

def check_number_length(number, length):
	min = pow(10,length) - 1
	max = pow(10,length + 1) - 1
	if(number <= min):
		return True
	if(number > max):
		return True
	return False

class Subject(models.Model):
	id_pass = models.IntegerField()
	id_tax = models.IntegerField()
	name = models.CharField(max_length = 200)
	serie_pass = models.CharField(max_length = 10)

class RealtyObject(models.Model):
	id_pass = models.IntegerField()
	id_cad = models.IntegerField()
	name = models.CharField(max_length = 200)
	adress = models.CharField(max_length = 400)

class MainRight(models.Model):
	subject = models.ForeignKey(Subject)
	realtyObject = models.ForeignKey(RealtyObject)

#ef search(str(name)):



class Issue(models.Model):
	main_right = models.ForeignKey(MainRight)
	description = models.CharField(max_length = 400)

class SecondaryRight(models.Model):
	subject = models.ForeignKey(Subject)
	realtyObject = models.ForeignKey(RealtyObject)
	description = models.CharField(max_length = 400)

class Request(models.Model):
	approved = models.BooleanField(default = False)
	subject_id_pass = models.IntegerField()
	subject_id_tax = models.IntegerField()
	subject_name = models.CharField(max_length = 200)
	object_id_pass = models.IntegerField()
	object_id_cad = models.IntegerField()
	object_name = models.CharField(max_length = 200)
	object_adress = models.CharField(max_length = 400)
	description = models.TextField()

# Create your models here.
