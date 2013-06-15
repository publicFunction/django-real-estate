from django.forms import ModelForm
from banners.models import Banner

class BannerForm(ModelForm):
    class Meta:
        model = Banner
    
    def __init__(self, *args, **kwargs):
        super(BannerForm, self).__init__(*args, **kwargs)
        choices = [self.fields['page'].choices.__iter__().next()]
        for page in choices:
            choices.append(
                       (page.id,''.join(['-'*page.level, page.__unicode__()]))
            )
        self.fields['page'].choices = choices