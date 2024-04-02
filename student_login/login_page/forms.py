from django import forms
from django.contrib.auth.models import User
from .models import Student
from django.contrib.auth.forms import AuthenticationForm

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'doj': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email_id': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'aadhar_number': forms.TextInput(attrs={'class': 'form-control'}),
            #'photograph': forms.FileInput(attrs={'class': 'form-control-file'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control'}),
            'passed_out_year': forms.Select(attrs={'class': 'form-control'}),
            'stream': forms.Select(attrs={'class': 'form-control'}),
            'course_type': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'blood_group': forms.Select(attrs={'class': 'form-control'}),
            'graduation_type': forms.Select(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if len(phone_number) < 10:
            raise forms.ValidationError("Phone number must be at least 10 digits long.")
        if not phone_number.isdigit():
            raise forms.ValidationError("Phone number must contain only numeric characters.")

        return phone_number

    def clean_email_id(self):
        email_id = self.cleaned_data.get('email_id')
        if not email_id.endswith('@gmail.com'):
            raise forms.ValidationError("Email address must end with @gmail.com.")
        return email_id

    def clean_aadhar_number(self):
        aadhar_number = self.cleaned_data.get('aadhar_number')
        if len(aadhar_number) < 12  :
            raise forms.ValidationError("Aadhar number must be at least 12 digits long.")
        if not aadhar_number.isdigit():
            raise forms.ValidationError("Aadhar number must contain only numeric characters.")

        return aadhar_number

    '''def clean_photograph(self):
        photograph = self.cleaned_data.get('photograph')
        if photograph.size > 10 * 1024 * 1024:  # 10MB in bytes
            raise forms.ValidationError("Photograph size should be less than 10MB.")
        return photograph'''

    def clean_username(self):
        username = self.cleaned_data.get('username')
        email_id = self.cleaned_data.get('email_id')
        if not username.endswith('@gmail.com'):
            raise forms.ValidationError("Username must end with @gmail.com.")
        if username != email_id:
            raise forms.ValidationError("Username must be the same as email address.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        phone_number = self.cleaned_data.get('phone_number')
        if password != phone_number:
            raise forms.ValidationError("Password must be the same as phone number.")
        return password 

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    



