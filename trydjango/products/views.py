from multiprocessing import context
from django.shortcuts import redirect, render,get_object_or_404
from django.http import Http404
from .models import Product
from .forms import ProductForm,RawProductForm


def product_create_view(request):
    obj = Product.objects.get(id=2)
    form = ProductForm(request.POST or None,instance=obj)  
    if form.is_valid():
        form.save()
            
    return render(request, 'products/create.html', {'form': form} )


def product_detail_view(request, id):
    obj = get_object_or_404(Product,id=id)
    
    return render(request, 'products/detail.html',{'obj':obj} )


def product_delete_view(request, id):
    obj = get_object_or_404(Product,id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('home')
    return render(request, 'products/delete.html',{'obj':obj} )


def product_list_view(request):
    queryset = Product.objects.all()
    return render(request, 'products/list.html',{'object_list':queryset} )


def people_update_view(request, id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('social')
    return render(request, 'products/update.html', {'object':obj})

