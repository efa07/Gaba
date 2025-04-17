from django.shortcuts import render,get_object_or_404,redirect
from .models import Item, Category
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import NewItemForm, EditItemForm

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

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk,created_by=request.user)
    item.delete()
    return redirect('dashboard:index')


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('items:detail', pk=item.pk)
    else:
        form = EditItemForm(instance=item)
    context ={
        'form': form,
        'title': 'Edit Item',
        }
    return render(request, 'items/form.html', context)


def search(request):
    query = request.GET.get('query','')
    category_id = request.GET.get('category',0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_available=True)
    if category_id:
        items = items.filter(category_id=category_id)
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, "items/search.html", {
        "items": items,
        "query": query,
        "categories": categories,
        'category_id': category_id
    })