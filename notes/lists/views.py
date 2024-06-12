from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, list
# Create your views here.
def home_page(request):
    return render(request, 'home.html')


def view_list(request, list_id):
    List_user = list.objects.get(id = list_id)
    #items = Item.objects.filter(list = List_user)
    return render(request, 'list.html', {'list': List_user})

def new_list(request):
    List_user = list.objects.create()
    Item.objects.create(text = request.POST['item_text'], list = List_user)
    return redirect(f'/lists/{List_user.id}/')

def add_item(request, list_id):
    List_user = list.objects.get(id = list_id)
    Item.objects.create(text = request.POST['item_text'], list = List_user)
    return redirect(f'/lists/{List_user.id}/')