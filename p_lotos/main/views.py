from django.shortcuts import render
from .models import Genre

# Create your views here.





def show_genres(request):
    data = {
        'genres': Genre.objects.all(),
    }
    return render(request, "genres.html", context=data)
