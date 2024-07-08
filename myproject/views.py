
from django.shortcuts import render
from django.http import HttpResponse
 
def homepage(request):
    data= {
        'title':'home page',
        'bdata' : 'Welcome to myproject',
        'clist' : ['PHP','Java','Django'],
        'students': [
            {'id': 1, 'name': 'Ishan', 'roll_no': '018'},
            {'id': 2, 'name': 'sagar', 'roll_no': '030'},
            {'id': 3, 'name': 'Rojdeep', 'roll_no': '029'},
        ],
    }
    return render(request,"index.html",data)

from django.http import HttpResponse
def aboutus(request):
    return HttpResponse('Welcome to myproject')
from django.http import HttpResponse
def courseDetails(request,courseid):
    return HttpResponse(courseid)

