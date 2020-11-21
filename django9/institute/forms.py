from django import forms
from .models import enquariform
from multiselectfield import MultiSelectFormField

class enquary(forms.Form):
    name=forms.CharField(
        label='Enter Your Name ',
        widget=forms.TextInput(
            attrs={
                'class':'form-control','placeholder':'Enter Your Name..'

            }
        )
    )
    mobile = forms.IntegerField(
        label='Enter Your Mobile Number ',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Enter Your mobile number..'
            }
        )
    )
    email = forms.EmailField(
        label='Enter Your Email ID ',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Enter Your mail id..'
            }
        )
    )
    COURCES_CHOICE=(
        ('python','PYTHON'),
        ('django','DJANGO'),
        ('ui','UI'),
        ('flask','FLASK'),
        ('java','JAVA'),

    )
    course = MultiSelectFormField(choices=COURCES_CHOICE, label='select required cources')


    TRAINER_CHOICE = (
        ('narayana', 'NARAYANA'),
        ('srinivas', 'SRINIVAS'),
        ('rubi', 'RUBI'),
        ('rachna', 'RACHNA'),
        ('mohit', 'MOHIT')

    )
    trainer=MultiSelectFormField(choices=TRAINER_CHOICE,label='select required trainer')

    SHIFT_CHOICE = (
        ('morning', 'MORNING'),
        ('evening', 'EVENING'),
        ('night', 'NIGHT')

    )
    shift = MultiSelectFormField(choices=SHIFT_CHOICE, label='select required shift')

    LOCATION = (
        ('ameerpet', 'AMEERPET'),
        ('secundrabaad', 'SECANDRABAAD'),
        ('hyd', 'HYD'),
        ('begumpet', 'BEGUMPET')

    )
    location = MultiSelectFormField(choices=LOCATION, label='select required location')


    GENDER_CHOICE = (
        ('male','MALE'),
        ('female','FEMAIL')
    )
    gender=forms.ChoiceField(
        widget= forms.RadioSelect , choices= GENDER_CHOICE,label='select your gender'
    )

from django import forms
from multiselectfield import MultiSelectFormField


class entry_student(forms.Form):
    fname = forms.CharField(
        label='Enter Your First Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control' , 'placeholder':'Enter Your First Name...'
            }
        )
    )

    lname = forms.CharField(
        label='Enter Your Last Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Enter Your Last Name...'
            }
        )
    )

    company = forms.CharField(
        label='Enter Your Company Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Enter Your Name...'
            }
        )
    )
    location = forms.CharField(
        label='Enter Your Location',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Enter Your Name...'
            }
        )

    )

    email = forms.EmailField(
        label='Enter Your Email ID',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control','placeholder': 'Enter Your Email Address...'
            }
        )
    )

    mobile = forms.IntegerField(
        label='Enter Your Mobile number ',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Enter Your Mobile Number...'
            }
        )
    )

    salary = forms.IntegerField(
        label='Enter Your Salary',
        widget= forms.NumberInput(
            attrs={
                'class':'form-control', 'placeholder':'Enter Your Salary...'
            }
        )
    )

    QUALIFICATION = (
        ('ba', 'BA'),
        ('be', 'BE'),
        ('bsc', 'BSC'),
        ('bcom', 'BCOM'),
        ('c-cat', 'C-CAT'),

    )
    qualification = MultiSelectFormField(choices=QUALIFICATION, label='Select Required Cources')












