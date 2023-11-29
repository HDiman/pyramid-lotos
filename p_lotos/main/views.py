from django.shortcuts import render, redirect, get_object_or_404
from .models import Genre


# Create your views here

def create(request, id):
    if request.method == 'POST':
        return redirect('home')
    else:
        data = {
            'genres': Genre.objects.all(),
        }
        return render(request, "create.html", context=data)


def rename(request):
    # obj = get_object_or_404(Genre, name='Samanta')
    # obj.name = 'Sandra'
    # obj.save()
    return redirect('home')


def delete(request):
    # obj = Genre.objects.get(pk=7)
    # obj.delete()
    return redirect('home')


def show_genres(request):
    data = {
        'genres': Genre.objects.all(),
    }
    return render(request, "genres.html", context=data)
