from django.shortcuts import render,get_object_or_404,redirect
from .models import Item
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm
def detail(request,pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category = item.category, is_available=True).exclude(pk=item.pk)[0:3]
    context = {
        'item': item,
        'related_items': related_items,
    }
    return render(request, 'items/detail.html', context)


@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.user = request.user
            item.save()
            return redirect('items:detail', pk=item.pk)
        
    else:
        form = NewItemForm()
    context ={
        'form': form,
        'title': 'New Item',
        }
    return render(request, 'items/form.html', context)