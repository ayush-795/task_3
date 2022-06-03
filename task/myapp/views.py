from django.shortcuts import render, redirect
from myapp.decorators import moderator_required, student_required
from myapp.forms import *
from .models import *
from django.contrib.postgres import *
from django.http import HttpResponse
import csv
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


# Create your views here.
def index(request):
    return render(request,'index.html',)

@login_required
@moderator_required
def list_items(request):
    title='List of items'
    form=StockSearchForm(request.POST or None)
    queryset=Stock.objects.all()
    context={
        "title":title,
        "queryset":queryset,
        "form":form
    }
    if request.method == 'POST':
        queryset=Stock.objects.filter(item_name__icontains=form['item_name'].value())
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of stock.csv"'
            writer = csv.writer(response)
            writer.writerow(['CATEGORY', 'ITEM NAME', 'QUANTITY'])
            instance = queryset
            for stock in instance:
             writer.writerow([stock.category, stock.item_name, stock.quantity])
            return response
        context={
            "form":form,
            "title":title,
            "queryset":queryset,
        }
    return render(request,'list_items.html',context)

@login_required
@moderator_required
def add_items(request):
    form=StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/list_items')
    context={
        "form":form,
        'title':"Add item",
    }
    return render(request,'add_items.html',context)

@login_required
@moderator_required
def update_items(request,pk):
    queryset=Stock.objects.get(id=pk)
    form=StockUpdateForm(instance=queryset)
    if request.method == 'POST' :
        instance=form.save(commit=False)
        instance.issue_by="None"
        instance.issue_quantity=0
        form= StockUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/list_items')
            
    context={
        'form':form
    }
    return render(request, 'add_items.html', context)

@login_required
@moderator_required
def delete_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('/list_items')
	return render(request, 'delete_items.html')


@login_required
@student_required
def stock_detail(request, pk):
	queryset = Stock.objects.get(id=pk)
	context = {
		"title": queryset.item_name,
		"queryset": queryset,
	}
	return render(request, "stock_detail.html", context)


@login_required
@student_required
def issue_items(request, pk):
    queryset= Stock.objects.get(id=pk)
    form = IssueForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance =form.save(commit=False)
        if (instance.quantity < instance.issue_quantity):
            messages.success(request, "Issued item doesn't have enough units to issue")
        else:
            instance.quantity-=instance.issue_quantity
            instance.issue_by=str(request.user)
            instance.save()
            send_mail=(
                'Issue Notice',
                'Hey, You have issued',
                'f20210772@pilani.bits-pilani.ac.in',
                ['TO@gmail.com'],
            )
    
        return redirect('/stock_detail/' +str(instance.id))
    context={
        "title":'Issue' + str(queryset.item_name),
        "queryset": queryset,
        "form":form,
        "username":'Issue By:' + str(request.user),
    }
    return render (request,'add_items.html',context)


@login_required
@moderator_required
def list_history(request):
	header = 'LIST OF ITEMS'
	queryset = StockHistory.objects.all()
	context = {
		"header": header,
		"queryset": queryset,
	}
	return render(request, 'list_history.html',context)


@login_required
@student_required
def list_itemss(request):
    title='List of items'
    form=StockSearchForm(request.POST or None)
    queryset=Stock.objects.all()
    context={
        "title":title,
        "queryset":queryset,
        "form":form
    }
    if request.method == 'POST':
        queryset=Stock.objects.filter(item_name__icontains=form['item_name'].value())
        context={
            "form":form,
            "title":title,
            "queryset":queryset,
        }
    return render(request,'list_itemss.html',context)


