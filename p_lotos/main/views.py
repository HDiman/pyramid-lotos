from django.shortcuts import render, redirect, get_object_or_404
from .models import Genre


def create(request):
    if request.method == 'POST':
        child = request.POST.get('child')
        parent = request.POST.get('item')
        if len(child) != 0:
            obj = Genre.objects.get(pk=parent)
            Genre.objects.create(name=child, parent=obj)
        return redirect('show_genres')
    else:
        data = {'genres': Genre.objects.all()}
        return render(request, "create.html", context=data)


def rename(request):
    if request.method == 'POST':
        new_name = request.POST.get('new_name')
        item = request.POST.get('item')
        if len(new_name) != 0:
            obj = Genre.objects.get(pk=item)
            obj.name = new_name
            obj.save()
        return redirect('show_genres')
    else:
        data = {'genres': Genre.objects.all()}
        return render(request, "rename.html", context=data)


def delete(request):
    if request.method == 'POST':
        del_item = request.POST.get('item')
        obj = Genre.objects.get(pk=del_item)
        obj.delete()
        return redirect('show_genres')
    else:
        data = {'genres': Genre.objects.all()}
        return render(request, "delete.html", context=data)


def show_genres(request):
    main_id = 30
    main_name = Genre.objects.get(pk=main_id)
    main_children = get_children(Genre,)



    data = {
        'main_name': main_name.name,
        'main_child': main_children
    }
    return render(request, "genres.html", context=data)







# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Here is starting to move DB to Board

def edit(request, id):
    grid = Genre.objects.get(id=id)
    if request.method == 'POST':
        # form = request.POST
        userform_0 = request.POST.get('item_0')
        userform_1 = request.POST.get('item_1')
        userform_2 = request.POST.get('item_2')
        userform_3 = request.POST.get('item_3')
        userform_4 = request.POST.get('item_4')
        userform_5 = request.POST.get('item_5')
        userform_6 = request.POST.get('item_6')
        userform_7 = request.POST.get('item_7')
        userform_8 = request.POST.get('item_8')

        if len(userform_0) != 0:
            grid.item_0 = userform_0
        if len(userform_1) != 0:
            grid.item_1 = userform_1
        if len(userform_2) != 0:
            grid.item_2 = userform_2
        if len(userform_3) != 0:
            grid.item_3 = userform_3
        if len(userform_4) != 0:
            grid.item_4 = userform_4
        if len(userform_5) != 0:
            grid.item_5 = userform_5
        if len(userform_6) != 0:
            grid.item_6 = userform_6
        if len(userform_7) != 0:
            grid.item_7 = userform_7
        if len(userform_8) != 0:
            grid.item_8 = userform_8
        grid.save()
        return redirect('home')
    else:
        data = {
            'id': id,
            'grid_0': Genre.objects.all()[0],
            'grid_1': Genre.objects.all()[1],
            'grid_2': Genre.objects.all()[2],
            'grid_3': Genre.objects.all()[3],
            'grid_4': Genre.objects.all()[4],
            'grid_5': Genre.objects.all()[5],
            'grid_6': Genre.objects.all()[6],
            'grid_7': Genre.objects.all()[7],
            'grid_8': Genre.objects.all()[8],
        }
        return render(request, 'edit.html', context=data)


def index(request):
    main_id = 30
    main_name = Genre.objects.get(pk=main_id)



    data = {
        'id': main_id,
        'main_name': main_name.name
    }
    return render(request, 'index.html', context=data)














# Archive @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# def show_genres(request):
#     data = {
#         'genres': Genre.objects.all()
#     }
#     return render(request, "genres.html", context=data)