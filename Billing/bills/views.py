# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.forms.utils import ErrorDict

from django.shortcuts import render
from .forms import InfoForm
from .models import Customer, Product


# Create your views here.

def index(request):
    form = InfoForm(request.POST or None)

    customername = request.POST.get('customername')
    mobilenumber = request.POST.get('mobilenumber')
    customerid = request.POST.get('customerid')

    #Check if the customer is existing in database

    print('Searching for customer',customerid) 

    try:
        customer = Customer.objects.get(customer_idt=customerid)
        print('cust present') 
        request.session['isNew'] = False
    except Customer.DoesNotExist as e:   
        print('cust not present') 
        request.session['isNew'] = True
        if form.is_valid():
            print('for is valid') 
            cus = Customer(customer_name=customername,customer_mob_no=mobilenumber,customer_idt=customerid)
            cus.save()
            print(form.cleaned_data)



    product = Product.objects.all()
    product_no = Product.objects.all().count()     
    mylist = []
    # db store
    context = {
        'title': 'VIT Billing System',
        'Name': customername,
        'mobilenumber': mobilenumber,
        'products':product,
        'product_no':product_no,
        'mylist':mylist
    }

    if request.method == "POST" and customerid != None:
        return render(request, "bills/menu.html", context)

    return render(request, "bills/index.html", {'form': form, 'title': 'VIT Billing System'})


def cal_amount(request):
    print("cal_amount")
    amount = 0.0
    count = 0

    isNew = False

    if(request.session['isNew']):
        request.session['isNew'] = False
        isNew = True
    else:
        isNew = False

    print('========== Is Customer New ? :',isNew)

    username = request.POST.get('username')
    mobilenumber = request.POST.get('mobilenumber')

    products = Product.objects.all()
    total_count = Product.objects.all().count()
    for p in products:
        id = p.product_id
        q = request.POST.get('q_id_' + str(id))
        qly = request.POST.get('qlt_id_' + str(id))

        qlt_price = 0.0;
        if(qly == '1'):
            qlt_price = p.product_qlt1_price
        if(qly == '2'):
            qlt_price = p.product_qlt2_price
        if(qly == '3'):
            qlt_price = p.product_qlt3_price
       

        if q is not None and q != '' and float(q):
            q = float(q)
            amount += q * float(qlt_price)
            count += 1

        discount = 0.0
        cashdiscount = 0.0
        final_amount = amount

        if amount > 10000 :
            discount = (amount*0.01)
            final_amount = amount - discount
            if (isNew != True):
                cashdiscount = (amount*0.012)

    context = {
        'count': count,
        'amount': amount,
        'discount': discount,
        'final_amount':final_amount,
        'cash_discount':cashdiscount
    }

    return render(request, "bills/bills.html", context)

