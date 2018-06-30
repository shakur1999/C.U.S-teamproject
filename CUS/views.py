from django.shortcuts import render, get_object_or_404, redirect
from .forms import cusform
from .models import cusapp

def add_cusapp(request):
    if request.method == "POST":
        form = cusform(request.POST)
        if form.is_valid():
            cusapp_item = form.save(commit=False)
            cusapp_item.save()
            return redirect('maps/' + str(cusapp_item.id))
    else:
        form = cusform()
    return render(request, 'cusapp/index.html', {'form': form})

def maps(request, id=None):
    cus = get_object_or_404(cusapp, id=id)
    return render(request, 'cusapp/maps.html', { 'cus': cus })

# def login_reg(request):
#     context = {
#
#     }
#     return render(request, 'cusapp/login_reg', context)
#
# def homepage(request):
#     context = {
#     }
#     return render(request, 'cusapp/index2.html', context)

# def edit_cusapp(request, id=None):
#     item = get_object_or_404(Blog, id=id)
#     form = cusform(request.POST or None, instance=item)
#     if form.is_valid():
#         form.save()
#         return render(request, 'cusapp/index.html', {'form': form})
#
#
# def cusapp(request):
#     context = {
#
#     }
#     return render(request, 'cusapp/index.html', context)
