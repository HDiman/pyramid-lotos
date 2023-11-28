from django.shortcuts import render, redirect, get_object_or_404

from .models import Genre

# Create your views here.

# Rename objects
def rename(request):
    obj = get_object_or_404(Genre, name='Samanta')
    obj.name = 'Sandra'
    obj.save()
    return redirect('home')

# Rename objects
def delete(request):
    obj = get_object_or_404(Genre, name='Samanta')
    obj.name = 'Sandra'
    obj.save()
    return redirect('home')



def show_genres(request):

    # # Rename objects
    # obj = get_object_or_404(Genre, name='Samanta')
    # obj.name = 'Sandra'
    # obj.save()

    # children = samanta.get_children()



    data = {
        'genres': Genre.objects.all(),
        # 'item': samanta,
        # 'children': children,
    }
    return render(request, "genres.html", context=data)
