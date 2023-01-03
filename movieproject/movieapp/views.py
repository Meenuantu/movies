from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import Movieform
from .models import movie


# Create your views here.
def index(request):
    movie1=movie.objects.all()
    context={'movie_list':movie1

    }
    return render(request,'request.html',context)

def detail(request,movie_id):
    m1=movie.objects.get(id=movie_id)
    return render(request,'details.html',{'mov':m1})
    #return HttpResponse("This is movie %s" %movie_id )

def add_movie(request):
    if request.method=='POST' :
        v_name=request.POST.get('movie_name')
        v_desc = request.POST.get('desc')
        v_year=request.POST.get('movie_year')
        v_img = request.FILES['img']
        v_mov=movie(movie_name=v_name,desc=v_desc,movie_year=v_year,img=v_img)
        v_mov.save()
        return redirect('/')

    return render(request,'movie.html')

def update_movie(request,movie_id):
    v_movie=movie.objects.get(id=movie_id)
    v_form=Movieform(request.POST or None, request.FILES, instance=v_movie)
    if v_form.is_valid():
        v_form.save()
        return redirect('/')

    return render(request,'edit_movie.html',{'form':v_form,'movie':v_movie})

def delete(request,movie_id):
    if request.method=='POST':
        v_movie=movie.objects.get(id=movie_id)
        v_movie.delete()
        return redirect('/')
    return render(request,'delete.html')






