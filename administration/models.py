from django.db import models
from django import forms
from datetime import datetime
from stdimage import StdImageField



# Create your models here
CHOICES=[('M','MALE'),
         ('F','FEMALE')]

class Student(models.Model):
	name=models.CharField(max_length=100)
	surname=models.CharField(max_length=100)
	clas=models.IntegerField()
	father=models.CharField(max_length=100)
	rollno=models.IntegerField()
	gander = models.CharField(max_length=1, choices=CHOICES, null=True)
	mobile=models.CharField(max_length=100)
	fee=models.IntegerField()

	def fullname(self):
		return (self.name+self.surname)
	def __unicode__(self):
		return self.father + self.name
	def __str__(self):
		return "%s name" % self.name


class Fee(models.Model):
	installment=models.IntegerField()
	date=models.DateField(default=datetime.now)
	student= models.ForeignKey(Student, on_delete=models.CASCADE,related_name='users')

	def __str__(self):
		return "%s the restaurant" % self.installment
class Common(models.Model):
	slider=models.ImageField(null=True)
	slider1=models.ImageField(null=True)
	slider2=models.ImageField(null=True)
class Content(models.Model):
	where=models.CharField(max_length=2000)
	text=models.CharField(max_length=100)
	date1=models.DateField(default=datetime.now)
	text1=models.CharField(max_length=100)
	date2=models.DateField(default=datetime.now)
	photo=StdImageField(variations={'thumbnail': (250, 178)}) 
	photo1=StdImageField(variations={'thumbnail': (250, 178)})
	photo2=StdImageField(variations={'thumbnail': (250, 178)})
	photo3=StdImageField(variations={'thumbnail': (250, 178)})
	slider=models.ForeignKey(Common,on_delete=models.CASCADE,related_name='common')



class ContentForm(forms.ModelForm):
	class Meta:
		model=Content
		fields='__all__'


class Contact(models.Model):
	name=models.CharField(max_length=100)
	mobile=models.CharField(max_length=10)
	email=models.EmailField(null=False,blank=False,unique=False)
	message=models.CharField(max_length=500)

	def __str__(self):
		return self.name

class ContactForm(forms.ModelForm):
	class Meta:
		model=Contact
		fields='__all__'



class StudentForm(forms.ModelForm):
	class Meta:
		
		model=Student

		fields=['name','surname','clas','father','rollno','gander','mobile','fee']



