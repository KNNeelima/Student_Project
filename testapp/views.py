from django.shortcuts import render
from testapp import forms
# Create your views here.
def Student_View(request):
    form=forms.StudentForm()
    if request.method=='POST':
        form=forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Form is working fine and data is saved in the DB")
            return render(request,'testapp/register.html',{'form':form})
    return render(request,'testapp/register.html',{'form':form})
