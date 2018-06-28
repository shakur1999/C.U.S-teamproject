from django.shortcuts import render, get_object_or_404, redirect
from .forms import cusform
from .models import cusapp

def homepage(request):
    context = {

    }
    return render(request, 'cussapp/index2.html', context)


def add_cusapp(request):
    if request.method == "POST":
        form = cusform(request.POST)
        if form.is_valid():
            cusapp_item = form.save(commit=False)
            cusapp_item.save()
            return redirect('/cusapp/' + str(cusapp.id) + '/')
    else:
        form = cusform()
    return render(request, 'cusapp/index.html', {'form': form})

def edit_cusapp(request, id=None):
    item = get_object_or_404(Blog, id=id)
    form = cusform(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return render(request, 'cusapp/index.html', {'form': form})


def cusapp(request):
    context = {

    }
    return render(request, 'cusapp/index.html', context)

def maps(request):
    return render(request, 'cusapp/maps.html', {})
