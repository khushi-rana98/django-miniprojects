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


# displaying python data structures in views only
# since view can hold any python object, but browser only understands
# text. so every structure has to b turned into string(html or plain text)
# or into json before leaving the view. 
# 2 tools--
# 1  '...'.join(list)-->build html
# 2  jsonResponse()--> json

# list
def show_list(request):
    subjects=['python','flask','django']
    items=''.join(f'<li>{s}</li>' for s in subjects)
    html=f'<h2>Subjects {len(subjects)}</h2><ul>{items}</ul>'
    return HttpResponse(html)

# json response
def show_list2(request):
    subjects=["abc","def","ghi"]
    return JsonResponse({
        'total':len(subjects),
        'subjects':subjects
    })

# tuple
def show_tuple(request):
    points=('CSE',4,'B.tech')
    # rows=''.join(f'<li>{p}</li>' for p in points)
    # return HttpResponse(f'<ul>{rows}</ul>')
    return JsonResponse(list(points),safe=False)