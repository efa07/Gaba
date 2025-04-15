from django.shortcuts import render
from items.models import Item,Category
from .forms import SignupForm

# Create your views here.
def index(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    context = {
        'items': items,
        'categories': categories
    }
    return render(request, 'core/index.html', context)

def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')

def signup(request):
    form = SignupForm()

    return render(request, 'core/signup.html', {'form': form})