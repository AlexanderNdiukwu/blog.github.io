from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator


class tags(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)

    def __str__ (self):
        return self.name
    
    
    
    
class movie(models.Model):
    title = models.CharField(max_length=100)
    comment = models.TextField(max_length=100)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)], 
        default=1
    )
    date = models.DateField(auto_now_add=True )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts',null=True, blank=True)
    tag = models.ManyToManyField(tags,blank=True)
    
    
    def __str__(self):
        return self.title 
    
    
class profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE )
    bio=models.TextField(blank=True,null=True,max_length=100)
    image= models.ImageField(default='imag.png', upload_to='Profile',null=True,blank=True)
    
    def __str__(self):
        return self.user.username
    




    
















