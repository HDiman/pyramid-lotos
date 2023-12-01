def show_genres(request):
    # data = {
    #     'genres': Genre.objects.all()
    # }
    # return render(request, "genres.html", context=data)
    main_id = 30
    item0_0 = Genre.objects.get(pk=main_id)
    item0_0_children = item0_0.get_children()
    item_num = len(item0_0_children)
    if item_num < 8:
        iter_num = 8 - item_num
        for i in range(iter_num):
            Genre.objects.create(name='-', parent=item0_0)



def index(request):
    id = 30
    item0_0 = Genre.objects.get(pk=id)
    item0_0_children = item0_0.get_children()
    item_num = len(item0_0_children)
    if item_num < 8:
        num = eight(id)
        item0_0 = Genre.objects.get(pk=id)
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