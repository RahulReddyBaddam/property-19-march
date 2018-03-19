from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from accounts.models import UserProfile
from phonenumber_field.modelfields import PhoneNumberField
from mysite.models import Site
from geoposition.fields import GeopositionField

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username',
                'first_name',
                'last_name',
                'email',
                'password1',
                'password2',
            )

    def save(self,commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(widget = forms.TextInput(
            attrs = {
            'class' :'form-control',
            'placeholder' : "First Name"
            }
        ))
    last_name = forms.CharField(widget = forms.TextInput(
                    attrs = {
                    'class' :'form-control',
                    'placeholder' : "Last Name"
                    }
                ))
    email = forms.CharField(widget = forms.EmailInput(
                            attrs = {
                            'class' :'form-control',
                            'placeholder' : "Email Id"
                            }
                        ))
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
        )


class ProfileForm(forms.ModelForm):
    des = forms.CharField(widget = forms.TextInput(
        attrs = {
        'class' :'form-control',
        'placeholder' : "Description"
        }
        ))
    phone = PhoneNumberField()


    class Meta:
        model = UserProfile
        fields = ('des', 'phone',)


class SiteForm(forms.ModelForm):
    CHOICES = (
        ('apartments','Apartments'),
        ('houses','Houses'),
        ('land','Land'),
    )
    position = GeopositionField()
    title = forms.CharField(max_length=200)
    descrip = forms.CharField(max_length=300)
    cost = forms.DecimalField(decimal_places=2,max_digits=20)

    class Meta:
        model = Site
        fields = (
        'title',
        'descrip',
        'cost',
        'position',
        'category',
        )
