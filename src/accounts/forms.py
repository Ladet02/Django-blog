
from django.contrib.auth import get_user_model
User = get_user_model()


class SignUpForm(forms.ModelForm):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email_address = forms.EmailField()
    password = forms.CharField()
    confirm_password = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email_address', 'password', 'confirm_password')
