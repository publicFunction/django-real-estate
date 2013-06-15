from django.forms.models import ModelForm
from property.models import Property
 
class searchForm(ModelForm):
    class Meta:
        model = Property
        
