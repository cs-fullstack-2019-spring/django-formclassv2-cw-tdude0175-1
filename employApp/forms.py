from django import forms

#  Employee Application. Give it a name, date of birth, position applying to, and salary.
class EmployeeAppForm(forms.Form):
    name= forms.CharField()
    dateOfBirth= forms.DateField()
    position= forms.CharField()
    salary= forms.DecimalField()