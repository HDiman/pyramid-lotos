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