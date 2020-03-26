from django.contrib import admin
from .models import Supplier, Customer, Transport, Bank, PurchaseEntry
from datetime import date

# Register your models here.
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    actions = None
    readonly_fields = ['ID']
    fields = ['ID', 'name', 'address1', 'address2', 'city', 'pincode',
              'phone_number', 'mobile_number', 'GST Number', 'agent_commission']
    list_display = ['name', 'city', 'mobile_number']
    search_fields = ['name', 'city']

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
    fields = ['ID', 'name', 'address1', 'address2', 'city', 'pincode',
              'phone_number', 'mobile_number', 'GST Number', 'max_due_date']
    list_display = ['name', 'city', 'mobile_number']
    search_fields = ['name', 'city']

    def ID(self, obj):
        if obj.id is None:
            row = Customer.objects.all().order_by('-id')[:1]
            if row:
                return row[0].id + 1
            else:
                return 0
        else:
            return obj.id

    def get_form(self, request, obj=None, **kwargs):
        form = super(SupplierAdmin, self).get_form(request, obj, kwargs)
        form.fields['supplier'].queryset = Supplier.objects.filter(name_iexact='name')
        return form


admin.site.register(Transport)
admin.site.register(Bank)


@admin.register(PurchaseEntry)
class PurchaseEntryAdmin(admin.ModelAdmin):
    actions= None

    list_display=['S_No', 'supplier', 'Bill No', 'Goods Value', 'transport']
    readonly_fields = ['S_No', 'Created On','Total Value']

    def S_No(self, obj):
        if obj.id is None:
            row = PurchaseEntry.objects.all().order_by('-id')[:1]
            if row:
                return row[0].id + 1
            else:
                return 0
        else:
            return obj.id

    # def Created_On(self, obj):
    #     if obj.id is None:
    #         print('today',date.today)
    #         return date.today

    #def total_value_calc(self, obj):


    fields = ['S_No', 'Created On', 'Bill No', 'Bill date', 'supplier', 'Goods Value', 'Discount', 'IGST', 'CGST',
              'SGST', 'Total Value', 'transport', 'LR No', 'LR date', 'Fright', 'Booking Station', 'customer', 'Delivery date']
