from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

class EditProfileForm(forms.ModelForm):
    # email = forms.
    class Meta:
        model = User
        fields = ('email', 'phone', 'fullname', 'address', 'zipcode', 'bio')
