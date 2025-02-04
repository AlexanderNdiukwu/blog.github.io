from django import forms 
from django.contrib.auth.models import User
from  django.contrib.auth.forms import UserCreationForm
from .models import movie,profile



class Register(UserCreationForm):
 
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    
    
class create_blog (forms.ModelForm):
    class Meta :
        model = movie
        fields = ['title', 'comment','rating','tag']
        
    
        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder':'Movie Title','class':'widget1'}
            ),
                'comment': forms.Textarea(
                attrs={'placeholder':'write your comment here','class':'widget2'}
            ),
               'rating': forms.NumberInput(
                attrs={'placeholder':'rate the movie ','class':'widget3'}
            ), 
        }
        
    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 1 or rating > 10:
            raise forms.ValidationError('Rating must be between 1 and 10.')
        return rating
    
    
    

class upload_img(forms.ModelForm): 
    class Meta:
        model = profile
        fields = ['image','bio']


class upload_profile(forms.ModelForm): 
    class Meta:
        model = User
        fields = ['username','email']
    
    
