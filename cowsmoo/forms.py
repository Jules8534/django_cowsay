from django import forms
from .models import CowsMooText
    
class  MooText(forms.ModelForm):
    class Meta:
        model = CowsMooText
        fields = ('text',)
        
      
