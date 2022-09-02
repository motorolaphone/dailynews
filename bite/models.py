from django.db import models

class contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=255)
    dt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
    	return self.full_name