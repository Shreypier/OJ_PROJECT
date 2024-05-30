from django.shortcuts import render
from Online_Compiler.forms import submissionform
from home.models import problem
from django.http import HttpResponse
from Online_Compiler.models import submission
from django.template import loader
from home.models import problem
# Create your views here

def problem_page(request):
    if request.method =='POST':
         language=request.POST['language']
         code=request.POST['code']
         input_data=request.POST['input']

         new=submission(language=language ,code=code,input_data=input_data) 
         new.save()
         sub=new 
         context={
             'sub':sub
         }
         return render(request,'result.html',context)
    
    else:
        
        template=loader.get_template("result.html")
        context={}
        return HttpResponse(template.render(context,request))