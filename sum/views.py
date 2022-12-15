from django.shortcuts import render
from django.http import HttpResponse
from .models import patient, issue, detail
# Create your views here.
def min(request):
    context ={
        "data":"Gfg is the best",
        "list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "message":'this is redirecting to another'
    }
    return render(request, "home.html",context)



def index(request):
  mymembers = patient.objects.all().values()
  mynumber  = issue.objects.all().values()
  member    = detail.objects.all().values()

  context = {
    'mymembers': mymembers,
    'mynumber' : mynumber,
    'member'   : member

  }
  
  return render(request,'table.html',context)


'''def add(request):
  mynumber = issue.objects.all().values()
  context = {
        'mynumber' : mynumber,
  }
  return render(request,'table.html',context)

def sub(request):
  member = details.objects.all().values()
  context = {
        'member'   : member

  }
  return render(request,'table.html',context)
'''

