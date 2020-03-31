from django.contrib import admin
from .models import Supplier, Customer, Transport, Bank, PurchaseEntry, State, PaymentEntry
from datetime import date
import easy

# Register your models here.

#admin.site.site_header = 'SLTA'


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

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super(SupplierAdmin, self).get_form(request, obj, kwargs)
    #     form.fields['supplier'].queryset = Supplier.objects.filter(name_iexact='name')
    #     return form


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
    #raw_id_fields = ['customer', 'supplier']

    list_display = ['S_No', 'bill_no', 'bill_date', 'supplier', 'city',
                    'goods_val', 'd_percent', 'd_value_', 'tax', 'tax_value', 'total', 'transport', 'lr_no']
    readonly_fields = ['S_No']
    # fields = ['S_No', 'bill_no', 'bill_date', 'supplier', 'city',
    #         'goods_val', 'd_percent', 'd_value_', 'tax', 'tax_value', 'total', 'transport', 'lr_no']

    def total(self, obj):
        val = obj.goods_val

        # va = val - discount_value_()

        if obj.goods_val and obj.d_percent is not None:
            val = val - (val * obj.d_percent / 100)
        elif obj.goods_val and obj.d_value is not None:
            val = val - obj.d_value

        val = val + (val * 5 / 100)

        return val

    def d_value_(self, obj):
        if obj.d_value is not None:
            return obj.d_value
        elif obj.d_percent is not None:
            return (obj.goods_val * obj.d_percent / 100)

    def S_No(self, obj):
        if obj.id is None:
            row = PurchaseEntry.objects.all().order_by('-id')[:1]
            if row:
                return row[0].id + 1
            else:
                return 0
        else:
            return obj.id

    def tax(self, obj):

        if obj.supplier.city.lower().strip() == 'tamilnadu':
            return "C/S GST"
        else:
            return "I GST"

    def tax_value(self, obj):
        val = obj.goods_val

        if obj.goods_val and obj.d_percent is not None:
            val = val - (val * obj.d_percent / 100)
        elif obj.goods_val and obj.d_value is not None:
            val = val - obj.d_value

        return val * 5 / 100

        # if obj.i_gst_tax is not None:
        #     return "I GST"
        # elif obj.s_gst_tax is not None and obj.c_gst_tax is not None:
        #     return "C/S GST"

    def city(self, obj):
        return obj.supplier.city


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    actions = None
    search_fields = ['state_name', ]


@admin.register(PaymentEntry)
class PaymentEntryAdmin(admin.ModelAdmin):
    actions = None
    autocomplete_fields = ['supplier', 'bank']
