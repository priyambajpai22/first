from django.test import TestCase

# Create your tests here.


from .models import *

if Content.objects.filter(id=1):
	pass
else:
	Content(where='index',text='this is the best thing i see',photo='image.jpg')