from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Genre



def to_fill(id):
    # check if there are 8 leafs
    item = Genre.objects.get(pk=id)
    item_child = item.get_children()

    item_num = len(item_child)
    if item_num < 8:
        num = 8 - item_num
        for i in range(num):
            Genre.objects.create(name='-', parent=item)

    item_child = item.get_children()

    # add leafs to leafs
    for i in range(8):
        leaf = item_child[i]
        leaf_child = leaf.get_children()
        leaf_num = len(leaf_child)
        if leaf_num < 8:
            num = 8 - leaf_num
            for j in range(num):
                Genre.objects.create(name='-', parent=leaf)


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


def replace_parent(request):
    if request.method == 'POST':
        child = request.POST.get('child')
        parent = request.POST.get('parent')
        if len(child) != 0:
            parent_obj = Genre.objects.get(pk=parent)  # parent's object
            parents_children = parent_obj.get_children()  # parent of all 8 children
            child_obj = Genre.objects.get(pk=child)  # object of a new child
            for item in parents_children:  # checking each child
                if item.name == '-':  # check if there ia no child
                    child_obj.parent = parent_obj  # adapted child
                    child_obj.save()
                    # obj = Genre.objects.get(pk=item.id)
                    # obj.delete()
                    item.delete()
                    return redirect('show_genres')
        return redirect('show_genres')
    else:
        data = {'genres': Genre.objects.all()}
        return render(request, "replace_parent.html", context=data)


def delete(request):
    if request.method == 'POST':
        del_item = request.POST.get('item')
        obj = Genre.objects.get(pk=del_item)
        obj.delete()
        return redirect('show_genres')
    else:
        # children = Genre.objects.get(pk=80).get_children()
        # data = {'genres': children}
        data = {'genres': Genre.objects.all()}
        return render(request, "delete.html", context=data)


def show_genres(request):
    data = {
        'genres': Genre.objects.all()
    }
    return render(request, "genres.html", context=data)


def themes(request):
    if request.method == 'POST':
        item = request.POST.get('item')
        obj_small = Genre.objects.get(pk=4255)
        obj_small.name = item
        obj_small.save()
        obj_big = Genre.objects.get(pk=18563)
        obj_big.name = item
        obj_big.save()
        to_fill(item)
        return redirect('home')
    else:
        # item = Genre.objects.get(pk=80)
        item = Genre.objects.get(pk=11515)
        item_children = item.get_children()
        data = {
            'item': item,
            'children': item_children,
        }
        return render(request, "themes.html", context=data)


# ========================================================
# Here is starting to move DB to Board

def edit(request, loc_id):
    if request.method == 'POST':
        userform_0 = request.POST.get('item_0')
        userform_0_id = request.POST.get('item_0.id')
        userform_1 = request.POST.get('item_1')
        userform_1_id = request.POST.get('item_1.id')
        userform_2 = request.POST.get('item_2')
        userform_2_id = request.POST.get('item_2.id')
        userform_3 = request.POST.get('item_3')
        userform_3_id = request.POST.get('item_3.id')
        userform_4 = request.POST.get('item_4')
        userform_4_id = request.POST.get('item_4.id')
        userform_5 = request.POST.get('item_5')
        userform_5_id = request.POST.get('item_5.id')
        userform_6 = request.POST.get('item_6')
        userform_6_id = request.POST.get('item_6.id')
        userform_7 = request.POST.get('item_7')
        userform_7_id = request.POST.get('item_7.id')
        userform_8 = request.POST.get('item_8')
        userform_8_id = request.POST.get('item_8.id')

        if len(userform_0) != 0:
            obj = Genre.objects.get(pk=userform_0_id)
            obj.name = userform_0
            obj.save()
        if len(userform_1) != 0:
            obj = Genre.objects.get(pk=userform_1_id)
            obj.name = userform_1
            obj.save()
        if len(userform_2) != 0:
            obj = Genre.objects.get(pk=userform_2_id)
            obj.name = userform_2
            obj.save()
        if len(userform_3) != 0:
            obj = Genre.objects.get(pk=userform_3_id)
            obj.name = userform_3
            obj.save()
        if len(userform_4) != 0:
            obj = Genre.objects.get(pk=userform_4_id)
            obj.name = userform_4
            obj.save()
        if len(userform_5) != 0:
            obj = Genre.objects.get(pk=userform_5_id)
            obj.name = userform_5
            obj.save()
        if len(userform_6) != 0:
            obj = Genre.objects.get(pk=userform_6_id)
            obj.name = userform_6
            obj.save()
        if len(userform_7) != 0:
            obj = Genre.objects.get(pk=userform_7_id)
            obj.name = userform_7
            obj.save()
        if len(userform_8) != 0:
            obj = Genre.objects.get(pk=userform_8_id)
            obj.name = userform_8
            obj.save()
        return redirect('home')
    else:
        edit_id = Genre.objects.get(pk=4255)
        item_id = edit_id.name

        item0_0 = Genre.objects.get(pk=item_id)
        item0_0_child = item0_0.get_children()
        item0_1 = item0_0_child[0]
        item0_2 = item0_0_child[1]
        item0_3 = item0_0_child[2]
        item0_4 = item0_0_child[3]
        item0_5 = item0_0_child[4]
        item0_6 = item0_0_child[5]
        item0_7 = item0_0_child[6]
        item0_8 = item0_0_child[7]
        to_fill(item0_1.id)
        to_fill(item0_2.id)
        to_fill(item0_3.id)
        to_fill(item0_4.id)
        to_fill(item0_5.id)
        to_fill(item0_6.id)
        to_fill(item0_7.id)
        to_fill(item0_8.id)

        item1_0_child = item0_1.get_children()
        item1_0 = item0_1
        item1_1 = item1_0_child[0]
        item1_2 = item1_0_child[1]
        item1_3 = item1_0_child[2]
        item1_4 = item1_0_child[3]
        item1_5 = item1_0_child[4]
        item1_6 = item1_0_child[5]
        item1_7 = item1_0_child[6]
        item1_8 = item1_0_child[7]

        item2_0_child = item0_2.get_children()
        item2_0 = item0_2
        item2_1 = item2_0_child[0]
        item2_2 = item2_0_child[1]
        item2_3 = item2_0_child[2]
        item2_4 = item2_0_child[3]
        item2_5 = item2_0_child[4]
        item2_6 = item2_0_child[5]
        item2_7 = item2_0_child[6]
        item2_8 = item2_0_child[7]

        item3_0_child = item0_3.get_children()
        item3_0 = item0_3
        item3_1 = item3_0_child[0]
        item3_2 = item3_0_child[1]
        item3_3 = item3_0_child[2]
        item3_4 = item3_0_child[3]
        item3_5 = item3_0_child[4]
        item3_6 = item3_0_child[5]
        item3_7 = item3_0_child[6]
        item3_8 = item3_0_child[7]

        item4_0_child = item0_4.get_children()
        item4_0 = item0_4
        item4_1 = item4_0_child[0]
        item4_2 = item4_0_child[1]
        item4_3 = item4_0_child[2]
        item4_4 = item4_0_child[3]
        item4_5 = item4_0_child[4]
        item4_6 = item4_0_child[5]
        item4_7 = item4_0_child[6]
        item4_8 = item4_0_child[7]

        item5_0_child = item0_5.get_children()
        item5_0 = item0_5
        item5_1 = item5_0_child[0]
        item5_2 = item5_0_child[1]
        item5_3 = item5_0_child[2]
        item5_4 = item5_0_child[3]
        item5_5 = item5_0_child[4]
        item5_6 = item5_0_child[5]
        item5_7 = item5_0_child[6]
        item5_8 = item5_0_child[7]

        item6_0_child = item0_6.get_children()
        item6_0 = item0_6
        item6_1 = item6_0_child[0]
        item6_2 = item6_0_child[1]
        item6_3 = item6_0_child[2]
        item6_4 = item6_0_child[3]
        item6_5 = item6_0_child[4]
        item6_6 = item6_0_child[5]
        item6_7 = item6_0_child[6]
        item6_8 = item6_0_child[7]

        item7_0_child = item0_7.get_children()
        item7_0 = item0_7
        item7_1 = item7_0_child[0]
        item7_2 = item7_0_child[1]
        item7_3 = item7_0_child[2]
        item7_4 = item7_0_child[3]
        item7_5 = item7_0_child[4]
        item7_6 = item7_0_child[5]
        item7_7 = item7_0_child[6]
        item7_8 = item7_0_child[7]

        item8_0_child = item0_8.get_children()
        item8_0 = item0_8
        item8_1 = item8_0_child[0]
        item8_2 = item8_0_child[1]
        item8_3 = item8_0_child[2]
        item8_4 = item8_0_child[3]
        item8_5 = item8_0_child[4]
        item8_6 = item8_0_child[5]
        item8_7 = item8_0_child[6]
        item8_8 = item8_0_child[7]

        data = {
            'loc_id': loc_id,
            'item0_0': item0_0,
            'item0_1': item0_1,
            'item0_2': item0_2,
            'item0_3': item0_3,
            'item0_4': item0_4,
            'item0_5': item0_5,
            'item0_6': item0_6,
            'item0_7': item0_7,
            'item0_8': item0_8,

            'item1_0': item1_0,
            'item1_1': item1_1,
            'item1_2': item1_2,
            'item1_3': item1_3,
            'item1_4': item1_4,
            'item1_5': item1_5,
            'item1_6': item1_6,
            'item1_7': item1_7,
            'item1_8': item1_8,

            'item2_0': item2_0,
            'item2_1': item2_1,
            'item2_2': item2_2,
            'item2_3': item2_3,
            'item2_4': item2_4,
            'item2_5': item2_5,
            'item2_6': item2_6,
            'item2_7': item2_7,
            'item2_8': item2_8,

            'item3_0': item3_0,
            'item3_1': item3_1,
            'item3_2': item3_2,
            'item3_3': item3_3,
            'item3_4': item3_4,
            'item3_5': item3_5,
            'item3_6': item3_6,
            'item3_7': item3_7,
            'item3_8': item3_8,

            'item4_0': item4_0,
            'item4_1': item4_1,
            'item4_2': item4_2,
            'item4_3': item4_3,
            'item4_4': item4_4,
            'item4_5': item4_5,
            'item4_6': item4_6,
            'item4_7': item4_7,
            'item4_8': item4_8,

            'item5_0': item5_0,
            'item5_1': item5_1,
            'item5_2': item5_2,
            'item5_3': item5_3,
            'item5_4': item5_4,
            'item5_5': item5_5,
            'item5_6': item5_6,
            'item5_7': item5_7,
            'item5_8': item5_8,

            'item6_0': item6_0,
            'item6_1': item6_1,
            'item6_2': item6_2,
            'item6_3': item6_3,
            'item6_4': item6_4,
            'item6_5': item6_5,
            'item6_6': item6_6,
            'item6_7': item6_7,
            'item6_8': item6_8,

            'item7_0': item7_0,
            'item7_1': item7_1,
            'item7_2': item7_2,
            'item7_3': item7_3,
            'item7_4': item7_4,
            'item7_5': item7_5,
            'item7_6': item7_6,
            'item7_7': item7_7,
            'item7_8': item7_8,

            'item8_0': item8_0,
            'item8_1': item8_1,
            'item8_2': item8_2,
            'item8_3': item8_3,
            'item8_4': item8_4,
            'item8_5': item8_5,
            'item8_6': item8_6,
            'item8_7': item8_7,
            'item8_8': item8_8,
            }
        return render(request, 'edit.html', context=data)


def index(request):
    if request.method == 'POST':
        user_id = request.POST.get('item')  # number
        obj = Genre.objects.get(pk=4255)  # object
        obj.name = user_id  # replace number
        obj.save()

    # looking for parent
    num_of_obj = Genre.objects.get(pk=4255)
    child_obj = Genre.objects.get(pk=num_of_obj.name)
    parent_of_obj = child_obj.parent
    hi_id = Genre.objects.get(pk=18563)
    try:
        hi_id.name = parent_of_obj.id
        hi_id.save()
    except AttributeError:
        pass
        # hi_id.name = child_obj.id
        # hi_id.save()

    # to begin with
    hi_id = Genre.objects.get(pk=18563)
    try:  # check if object was deleted
        some_id = Genre.objects.get(pk=hi_id.name)
    except ObjectDoesNotExist:
        hi_id = Genre.objects.get(pk=18563)
        hi_id.name = 30
        hi_id.save()
        item_id = Genre.objects.get(pk=4255)
        item_id.name = 30
        item_id.save()

    # to current center
    item_id = Genre.objects.get(pk=4255)
    main_id = item_id.name
    to_fill(main_id)
    item0_0 = Genre.objects.get(pk=main_id)
    item0_0_child = item0_0.get_children()
    item0_1 = item0_0_child[0]
    item0_2 = item0_0_child[1]
    item0_3 = item0_0_child[2]
    item0_4 = item0_0_child[3]
    item0_5 = item0_0_child[4]
    item0_6 = item0_0_child[5]
    item0_7 = item0_0_child[6]
    item0_8 = item0_0_child[7]
    to_fill(item0_1.id)
    to_fill(item0_2.id)
    to_fill(item0_3.id)
    to_fill(item0_4.id)
    to_fill(item0_5.id)
    to_fill(item0_6.id)
    to_fill(item0_7.id)
    to_fill(item0_8.id)

    item1_0_child = item0_1.get_children()
    item1_0 = item0_1
    item1_1 = item1_0_child[0]
    item1_2 = item1_0_child[1]
    item1_3 = item1_0_child[2]
    item1_4 = item1_0_child[3]
    item1_5 = item1_0_child[4]
    item1_6 = item1_0_child[5]
    item1_7 = item1_0_child[6]
    item1_8 = item1_0_child[7]

    item2_0_child = item0_2.get_children()
    item2_0 = item0_2
    item2_1 = item2_0_child[0]
    item2_2 = item2_0_child[1]
    item2_3 = item2_0_child[2]
    item2_4 = item2_0_child[3]
    item2_5 = item2_0_child[4]
    item2_6 = item2_0_child[5]
    item2_7 = item2_0_child[6]
    item2_8 = item2_0_child[7]

    item3_0_child = item0_3.get_children()
    item3_0 = item0_3
    item3_1 = item3_0_child[0]
    item3_2 = item3_0_child[1]
    item3_3 = item3_0_child[2]
    item3_4 = item3_0_child[3]
    item3_5 = item3_0_child[4]
    item3_6 = item3_0_child[5]
    item3_7 = item3_0_child[6]
    item3_8 = item3_0_child[7]

    item4_0_child = item0_4.get_children()
    item4_0 = item0_4
    item4_1 = item4_0_child[0]
    item4_2 = item4_0_child[1]
    item4_3 = item4_0_child[2]
    item4_4 = item4_0_child[3]
    item4_5 = item4_0_child[4]
    item4_6 = item4_0_child[5]
    item4_7 = item4_0_child[6]
    item4_8 = item4_0_child[7]

    item5_0_child = item0_5.get_children()
    item5_0 = item0_5
    item5_1 = item5_0_child[0]
    item5_2 = item5_0_child[1]
    item5_3 = item5_0_child[2]
    item5_4 = item5_0_child[3]
    item5_5 = item5_0_child[4]
    item5_6 = item5_0_child[5]
    item5_7 = item5_0_child[6]
    item5_8 = item5_0_child[7]

    item6_0_child = item0_6.get_children()
    item6_0 = item0_6
    item6_1 = item6_0_child[0]
    item6_2 = item6_0_child[1]
    item6_3 = item6_0_child[2]
    item6_4 = item6_0_child[3]
    item6_5 = item6_0_child[4]
    item6_6 = item6_0_child[5]
    item6_7 = item6_0_child[6]
    item6_8 = item6_0_child[7]

    item7_0_child = item0_7.get_children()
    item7_0 = item0_7
    item7_1 = item7_0_child[0]
    item7_2 = item7_0_child[1]
    item7_3 = item7_0_child[2]
    item7_4 = item7_0_child[3]
    item7_5 = item7_0_child[4]
    item7_6 = item7_0_child[5]
    item7_7 = item7_0_child[6]
    item7_8 = item7_0_child[7]

    item8_0_child = item0_8.get_children()
    item8_0 = item0_8
    item8_1 = item8_0_child[0]
    item8_2 = item8_0_child[1]
    item8_3 = item8_0_child[2]
    item8_4 = item8_0_child[3]
    item8_5 = item8_0_child[4]
    item8_6 = item8_0_child[5]
    item8_7 = item8_0_child[6]
    item8_8 = item8_0_child[7]

    data = {
        # 'test': child_obj.id,  # for test purpose
        'hi_id': hi_id,
        'item0_0': item0_0,
        'item0_1': item0_1,
        'item0_2': item0_2,
        'item0_3': item0_3,
        'item0_4': item0_4,
        'item0_5': item0_5,
        'item0_6': item0_6,
        'item0_7': item0_7,
        'item0_8': item0_8,

        'item1_0': item1_0,
        'item1_1': item1_1,
        'item1_2': item1_2,
        'item1_3': item1_3,
        'item1_4': item1_4,
        'item1_5': item1_5,
        'item1_6': item1_6,
        'item1_7': item1_7,
        'item1_8': item1_8,

        'item2_0': item2_0,
        'item2_1': item2_1,
        'item2_2': item2_2,
        'item2_3': item2_3,
        'item2_4': item2_4,
        'item2_5': item2_5,
        'item2_6': item2_6,
        'item2_7': item2_7,
        'item2_8': item2_8,

        'item3_0': item3_0,
        'item3_1': item3_1,
        'item3_2': item3_2,
        'item3_3': item3_3,
        'item3_4': item3_4,
        'item3_5': item3_5,
        'item3_6': item3_6,
        'item3_7': item3_7,
        'item3_8': item3_8,

        'item4_0': item4_0,
        'item4_1': item4_1,
        'item4_2': item4_2,
        'item4_3': item4_3,
        'item4_4': item4_4,
        'item4_5': item4_5,
        'item4_6': item4_6,
        'item4_7': item4_7,
        'item4_8': item4_8,

        'item5_0': item5_0,
        'item5_1': item5_1,
        'item5_2': item5_2,
        'item5_3': item5_3,
        'item5_4': item5_4,
        'item5_5': item5_5,
        'item5_6': item5_6,
        'item5_7': item5_7,
        'item5_8': item5_8,

        'item6_0': item6_0,
        'item6_1': item6_1,
        'item6_2': item6_2,
        'item6_3': item6_3,
        'item6_4': item6_4,
        'item6_5': item6_5,
        'item6_6': item6_6,
        'item6_7': item6_7,
        'item6_8': item6_8,

        'item7_0': item7_0,
        'item7_1': item7_1,
        'item7_2': item7_2,
        'item7_3': item7_3,
        'item7_4': item7_4,
        'item7_5': item7_5,
        'item7_6': item7_6,
        'item7_7': item7_7,
        'item7_8': item7_8,

        'item8_0': item8_0,
        'item8_1': item8_1,
        'item8_2': item8_2,
        'item8_3': item8_3,
        'item8_4': item8_4,
        'item8_5': item8_5,
        'item8_6': item8_6,
        'item8_7': item8_7,
        'item8_8': item8_8,
    }
    return render(request, 'index.html', context=data)
