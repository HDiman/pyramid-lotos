from django.shortcuts import render, redirect
from .models import Genre

# Create your views here.


def rename(request):
    blues = Genre.objects.get(name='Blues')
    blues = 'Text'
    blues.save()
    return redirect('home')



def show_genres(request):
    # blues = Genre.objects.get(name='Blues')
    # blues = 'Text'
    # blues.save()
    # rock = Genre.objects.get(name='Sandra')
    # Genre.objects.delete(name="Why!", parent=rock)
    # sandra = Genre.objects.get(name='Sandra')
    # sandra.clear()


    data = {
        'genres': Genre.objects.all(),
    }
    return render(request, "genres.html", context=data)
