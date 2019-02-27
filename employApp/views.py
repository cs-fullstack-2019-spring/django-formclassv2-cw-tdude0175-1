from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeAppForm
# Create your views here.


# only need one function to hand and compare method of the form back to same page to get the information
def index(request):
    applicationForm = EmployeeAppForm

    if(request.method == 'POST'):
        print(request.POST) # only necessary for testing not really for requirements
        content = \
            {
                'form':applicationForm,
                'employee': request.POST
            }
        return render(request,'employApp/employeeList.html',content)
    else:
        content =\
            {
                'form':applicationForm
            }
        return render(request,'employApp/index.html',content)
