from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva
from .forms import ReservaForm

# Create your views here.

def reserva_criar(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('reserva_listar')
        else:
            print(form.errors)
    else:
        form = ReservaForm()

    return render(request, 'stands/form.html', {'form': form})

def reserva_listar(request):
    reservas = Reserva.objects.all().order_by('data_reserva')
    context ={
        'reservas': reservas
    }
    return render(request, 'stands/index.html',context)

def detalhe_reserva(request,id):
    reserva = Reserva.objects.get(id=id)
    context = {
        'reserva':reserva
    }
    return render(request,'stands/detalhe.html',context)

def reserva_edicao(request):
    reservas = Reserva.objects.all()
    context ={
        'reservas':reservas
    }
    return render(request, 'stands/reserva.html',context)

def reserva_editar(request,id):
    reserva = get_object_or_404(Reserva,id=id)
   
    if request.method == 'POST':
        form = ReservaForm(request.POST,instance=reserva)

        if form.is_valid():
            form.save()
            return redirect('reserva_edicao')
    else:
        form = ReservaForm(instance=reserva)

    return render(request,"stands/form.html",{'form':form})

def reserva_remover(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('reserva_edicao') 

