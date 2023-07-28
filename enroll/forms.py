from django import forms
from .models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'password']
        labels = {
            'name': 'Enter Your Name',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':"Eg: kts@gmail.com"}),
            'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control'})
        }