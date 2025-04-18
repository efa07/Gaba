from django.shortcuts import redirect, render,get_object_or_404
from items.models import Item
from .models import Message
from .forms import MessageContentForm

def new_message(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index', item_pk=item.pk)
    
    message = Message.objects.filter(item=item).filter(members__in=[request.user])
    if message:
        pass
    if request.method == "POST":
        form = MessageContentForm(request.POST)
        if form.is_valid():
            message = Message.objects.create(item=item)
            message.members.add(request.user)
            message.save()
            form.instance.message = message
            form.instance.created_by = request.user
            form.save()
            return redirect('dashboard:index', item_pk=item.pk)
    else:
        form = MessageContentForm()
    context = {
        'form': form,
        'item': item,
    }
    return render(request, 'message/new_message.html', context)