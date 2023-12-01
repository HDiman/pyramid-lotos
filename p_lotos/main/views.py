from django.shortcuts import render, redirect, get_object_or_404
from .models import Genre


def eight(id):
    main_id = id
    item0_0 = Genre.objects.get(pk=main_id)
    item0_0_children = item0_0.get_children()
    item_num = len(item0_0_children)
    if item_num < 8:
        iter_num = 8 - item_num
        for i in range(iter_num):
            Genre.objects.create(name='-', parent=item0_0)


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
        # parent = obj.parent
        obj.delete()
        # eight(parent.id)
        return redirect('show_genres')
    else:
        data = {'genres': Genre.objects.all()}
        return render(request, "delete.html", context=data)


def show_genres(request):
    data = {
        'genres': Genre.objects.all()
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
    eight(main_id)

    item0_0 = Genre.objects.get(pk=main_id)
    item0_0_children = item0_0.get_children()

    data = {
        'item0_0': item0_0.name,
        'item0_1': item0_0_children[0].name,
        'item0_2': item0_0_children[1].name,
        'item0_3': item0_0_children[2].name,
        'item0_4': item0_0_children[3].name,
        'item0_5': item0_0_children[4].name,
        'item0_6': item0_0_children[5].name,
        'item0_7': item0_0_children[6].name,
        'item0_8': item0_0_children[7].name,

        'item1_0': '-',
        'item1_1': '-',
        'item1_2': '-',
        'item1_3': '-',
        'item1_4': '-',
        'item1_5': '-',
        'item1_6': '-',
        'item1_7': '-',
        'item1_8': '-',

        'item2_0': '-',
        'item2_1': '-',
        'item2_2': '-',
        'item2_3': '-',
        'item2_4': '-',
        'item2_5': '-',
        'item2_6': '-',
        'item2_7': '-',
        'item2_8': '-',

        'item3_0': '-',
        'item3_1': '-',
        'item3_2': '-',
        'item3_3': '-',
        'item3_4': '-',
        'item3_5': '-',
        'item3_6': '-',
        'item3_7': '-',
        'item3_8': '-',

        'item4_0': '-',
        'item4_1': '-',
        'item4_2': '-',
        'item4_3': '-',
        'item4_4': '-',
        'item4_5': '-',
        'item4_6': '-',
        'item4_7': '-',
        'item4_8': '-',

        'item5_0': '-',
        'item5_1': '-',
        'item5_2': '-',
        'item5_3': '-',
        'item5_4': '-',
        'item5_5': '-',
        'item5_6': '-',
        'item5_7': '-',
        'item5_8': '-',

        'item6_0': '-',
        'item6_1': '-',
        'item6_2': '-',
        'item6_3': '-',
        'item6_4': '-',
        'item6_5': '-',
        'item6_6': '-',
        'item6_7': '-',
        'item6_8': '-',

        'item7_0': '-',
        'item7_1': '-',
        'item7_2': '-',
        'item7_3': '-',
        'item7_4': '-',
        'item7_5': '-',
        'item7_6': '-',
        'item7_7': '-',
        'item7_8': '-',

        'item8_0': '-',
        'item8_1': '-',
        'item8_2': '-',
        'item8_3': '-',
        'item8_4': '-',
        'item8_5': '-',
        'item8_6': '-',
        'item8_7': '-',
        'item8_8': '-',
    }
    return render(request, 'index.html', context=data)
