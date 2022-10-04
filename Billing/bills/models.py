# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.six import python_2_unicode_compatible
from django.db import models
# Create your models here.

@python_2_unicode_compatible
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=200,default="")
    customer_mob_no = models.CharField(max_length=200,default="")
    customer_idt =  models.CharField(max_length=7,default="")	

    def __str__(self):
        return self.customer_name

@python_2_unicode_compatible
class Product(models.Model):
	product_id = models.AutoField(primary_key=True)
	product_name = models.CharField(max_length=200)
	product_detail = models.CharField(max_length=200)
	product_code = models.CharField(max_length=4,default='0000')
	product_qlt1_price = models.DecimalField(max_digits=6, decimal_places=2,default=0.00)
	product_qlt2_price = models.DecimalField(max_digits=6, decimal_places=2,default=0.00)
	product_qlt3_price = models.DecimalField(max_digits=6, decimal_places=2,default=0.00)
	
	def __str__(self):
		return self.product_name
