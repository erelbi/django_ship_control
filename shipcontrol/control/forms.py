from django import forms
from .models import Information,Ship,Master,Engineer

class Infoform(forms.ModelForm):
    # master = forms.CharField(label='Enter your name',max_length=50)
    # name = forms.CharField(label='Enter your ship name',max_length=50)
    # imo = forms.CharField(label='Enter your ship  imo number',max_length=10)
    # mmsi = forms.CharField(label='Enter your ship mmsi number',max_length=10)
    # callsign = forms.CharField(label='Enter your ship callsign',max_length=10)
    # gross = forms.CharField(label='Enter your ship gross tonage',max_length=10)
    # deadweight = forms.CharField(label='Enter your ship deadweight',max_length=10)
    # buildyear = forms.CharField(label='Enter your ship build year',max_length=10)
    
    class Meta:
         model = Information 
         fields = ('captain', 'ship','imo','mmsi','callsign','gross','deadweight','buildyear')
         def save(self):
             data = self.cleaned_data

class Engineerdata(forms.ModelForm):
    class Meta:
        model = Engineer
        fields = ('national','limit')
        