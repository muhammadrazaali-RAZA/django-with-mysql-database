from django.db import models

class Userreg(models.Model):
	uname=models.TextField(max_length=191) 
	umail=models.TextField(max_length=100)
	pnum=models.TextField(max_length=100)
	mtstatus=models.TextField(max_length=100)
	gender=models.CharField(max_length=10)
	class Meta:
		db_table="userreg"