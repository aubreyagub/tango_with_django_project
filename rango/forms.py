from django import forms
from rango.models import Page, Category
<<<<<<< HEAD

=======
from django.contrib.auth.models import User
from rango.models import UserProfile

# form to make a new category
>>>>>>> 33d984ed32ceb5d6a787c45340fdcad21486b1eb
class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=Category.max_length_cat, help_text="Please enter the category name.")

    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)

<<<<<<< HEAD
=======
# form to make a new page
>>>>>>> 33d984ed32ceb5d6a787c45340fdcad21486b1eb
class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=Page.max_length_page,help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200,help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    # use to properly format urls from user in case they're wrong
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
<<<<<<< HEAD

=======
        
>>>>>>> 33d984ed32ceb5d6a787c45340fdcad21486b1eb
        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url
        return cleaned_data


    class Meta:
        model = Page
<<<<<<< HEAD
        exclude = ('category',)
=======
        exclude = ('category',)

# form to make a new user
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

# form to customise user account
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)
>>>>>>> 33d984ed32ceb5d6a787c45340fdcad21486b1eb
