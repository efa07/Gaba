from django.shortcuts import render,get_object_or_404
from items.models import Item,Category
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)
    category = Category.objects.all()
    context = {
        'items': items,
               'categories':category}

    return render(request, 'dashboard/index.html', context)


