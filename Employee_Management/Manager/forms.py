from django import forms
from phonenumber_field.modelfields import PhoneNumberField
from Manager.models import Employee,Work

class EmployeeForm(forms.ModelForm):
    # emid=forms.IntegerField()
    # joining=forms.DateField()
    # name=forms.CharField(max_length=256)
    # email=forms.EmailField(max_length=256)
    # contact=forms.CharField(max_length=256)
    # designation=forms.ModelChoiceField(queryset=Work.objects.all())
    class Meta():
        model=Employee
        fields='__all__'

        widgets= {
            'emid':forms.TextInput(attrs={'class':'form-group row form-control col-sm-1','placeholder':'ID'}),
            'joining':forms.TextInput(attrs={'class':'form-group row form-control col-sm-2','placeholder':'MM/DD/YYYY'}),
            'name':forms.TextInput(attrs={'class':'form-group row form-control col-sm-2','placeholder':'Enter Name'}),
            'email':forms.TextInput(attrs={'class':'form-group row form-control col-sm-3','placeholder':'Enter Email'}),
            'contact':forms.TextInput(attrs={'class':'form-group row form-control col-sm-2','placeholder':'98654XXXXX'}),
            'designation':forms.Select(attrs={'class':'form-group row form-control col-sm-3'}),
        }


class WorkForm(forms.ModelForm):
    jobid=forms.IntegerField()
    job=forms.CharField(max_length=256)
    creation=forms.DateField()

    class Meta():
        model=Work
        fields='__all__'
