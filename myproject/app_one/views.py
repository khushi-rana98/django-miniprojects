from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

from django.http import JsonResponse

from django.shortcuts import render

from django.shortcuts import redirect
# Create your views here.--http response
def greeting(request):
    hour=14
    if hour<12:
        msg="Good MOrning"
    else:
        msg="Good EVening"

    today=date.today().strftime('%A %d %B %Y')
    res=f'<h1>{msg}</h1><p>Happy {today}</p>'
    return HttpResponse(res)


# return json response-- use from django.http import JsonResponse
def student(request):
    data={'name':'John','age':30,'course':'B.Tech','college':'LPU'}
    return JsonResponse(data)

#render the page--type 3 response
def student2(request):
    # data stored in dictionary : it sends the python data
    # to html template
    data={
        'name':"Arya",
        'course':'B.Tech',
        'college':'LPU'
    }
    return render(request,'home.html',data)

# return redirect()--> it redirect the user from one 
# url to another url
def go(request):
    return redirect('welcome_page')

def welcome_view(request):
    return HttpResponse("<h2>hey!you have been redirected</h2>")
