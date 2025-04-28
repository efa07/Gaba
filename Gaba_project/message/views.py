from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import redirect, render,get_object_or_404,HttpResponse
from items.models import Item
from .models import Message
from .forms import MessageContentForm

def msg(request, item_pk) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:
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

            msg = form.save(commit=False)
            msg.message = message
            msg.created_by = request.user
            msg.save()

            return redirect('items:detail', pk=item_pk)
    else:
        form = MessageContentForm()
    return render(request, 'message/msg.html', {'form': form})
