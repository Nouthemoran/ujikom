from penjualan.models import MyModel
from django.shortcuts import render, redirect
from penjualan.forms import MyModelForm

# Create
from django.shortcuts import redirect

def create_mymodel(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('penjualan:read')
    else:
        form = MyModelForm()
    return render(request, 'penjualan/form.html', {'form': form})

# Read
def get_mymodel_by_kdjual(kdjual):
    mymodel = MyModel.objects.get(kdjual=kdjual)
    return mymodel

def get_all_mymodels(request):
    mymodels = MyModel.objects.all()
    return render(request, 'penjualan/tabel.html', {'mymodels': mymodels})

# Update
def update_mymodel(request,id):
    mymodel = MyModel.objects.get(pk=id)
    
    data = {
        'kdbrg' : mymodel.kdbrg,
        'nmbrg':  mymodel.nmbrg,
        'tgltrans': mymodel.tgltrans,
        'jumbrg': mymodel.jumbrg,
        'hargabrg': mymodel.hargabrg,
        'totalbyr': mymodel.totalbyr, 
    }
    
    penjualan_form = MyModelForm(request.POST or None, initial=data, instance=mymodel)
    
    if request.method == 'POST':
        if penjualan_form.is_valid():
            penjualan_form.save()
            
        return redirect('penjualan:read')
    
    context = {
        "penjualan_form": penjualan_form,
    }
            
    return render(request, 'penjualan/form.html', context)

# Delete
def delete_mymodel(kdjual):
    mymodel = MyModel.objects.get(kdjual=kdjual)
    mymodel.delete()
