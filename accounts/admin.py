from django.contrib import admin
from django.core.serializers import serialize
from .models import Supplier, Customer, Transport, Bank, PurchaseEntry, State, PaymentEntry
from datetime import date
import easy
import json

# Register your models here.

# admin.site.site_header = 'SLTA'


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    actions = None
    readonly_fields = ['ID']
    fields = ['ID', 'name', 'address1', 'address2', 'city', 'state', 'pincode',
              'phone_number', 'mobile_number', 'GST Number', 'agent_commission']
    list_display = ['name', 'city', 'mobile_number']
    search_fields = ['name', 'city']
    list_filter = ['city']
    autocomplete_fields = ['state']

    def ID(self, obj):
        if obj.id is None:
            row = Supplier.objects.all().order_by('-id')[:1]
            if row:
                return row[0].id + 1
            else:
                return 0
        else:
            return obj.id


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    actions = None
    readonly_fields = ['ID']
    fields = ['ID', 'name', 'address1', 'address2', 'city', 'state', 'pincode',
              'phone_number', 'mobile_number', 'GST Number', 'max_due_date']
    list_display = ['name', 'city', 'mobile_number']
    search_fields = ['name', 'city']
    autocomplete_fields = ['state']

    def ID(self, obj):
        if obj.id is None:
            row = Customer.objects.all().order_by('-id')[:1]
            if row:
                return row[0].id + 1
            else:
                return 0
        else:
            return obj.id


@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    search_fields = ['name']

    class Media:
        js = ('js/custom_script.js',)


@admin.register(PurchaseEntry)
class PurchaseEntryAdmin(admin.ModelAdmin):

    actions = None
    autocomplete_fields = ['supplier', 'customer', 'transport']
    list_display = ['S_No', 'bill_no', 'bill_date', 'supplier', 'city',
                    'goods_val', 'd_percent', 'd_value_', 'tax', 'tax_value', 'total', 'transport', 'lr_no', 'customer']
    readonly_fields = ['S_No', 'total_price',
                       'city', 'c_gst', 's_gst', 'i_gst']
    fields = ['S_No', ('bill_no', 'bill_date'), ('supplier', 'city'),
              'goods_val', ('d_percent', 'd_value', 'c_gst', 's_gst', 'i_gst'), 'total_price',  ('transport', 'lr_no'), 'lr_date', ('fright', 'booking_station'), ('customer', 'delivery_date')]

    suppliers = Supplier.objects.all()
    suppliers = serialize('json', suppliers, fields=['name', 'city'])

    def S_No(self, obj):
        if obj.id is None:
            row = PurchaseEntry.objects.all().order_by('-id')[:1]
            if row:
                return row[0].id + 1
            else:
                return 0
        else:
            return obj.id

    def total_price(self, obj):
        return '0'

    def tax_amount(self, obj):
        return 'tax'

    def c_gst(self, obj):
        return 'c_tax'

    def s_gst(self, obj):
        return 's_tax'

    def i_gst(self, obj):
        return 'i_tax'

    def tax(self, obj):
        # return "GST"
        if obj.id is None:
            return "GST"
        else:
            if obj.supplier.city.lower().strip() == 'tamilnadu':
                return "C/S GST"
            else:
                return "I GST"

    def city(self, obj):
        return obj.supplier.city

    def changeform_view(self, request, obj_id, form_url, extra_context=None):

        suppliers = Supplier.objects.all()
        states = State.objects.all()
        suppliers = serialize('json', suppliers, fields=[
            'name', 'city', 'state'])
        states = serialize('json', states)

        context = {
            'suppliers': suppliers
        }

        return super(PurchaseEntryAdmin, self).changeform_view(request, obj_id, form_url, context)

    class Media:
        js = ('js/purchase_entry_script.js',)


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    actions = None
    search_fields = ['state_name', ]
    list_display = ['S_No', 'state_name']

    def S_No(self, obj):
        if obj.id is None:
            row = PurchaseEntry.objects.all().order_by('-id')[:1]
            if row:
                return row[0].id + 1
            else:
                return 0
        else:
            return obj.id


@admin.register(PaymentEntry)
class PaymentEntryAdmin(admin.ModelAdmin):
    actions = None
    autocomplete_fields = ['supplier', 'bank']
