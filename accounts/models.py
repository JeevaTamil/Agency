from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

# Create your models here.


class State(models.Model):
    state_name = models.CharField(max_length=50)

    def __str__(self):
        return self.state_name


class Supplier(models.Model):
    #supplier_id = models.AutoField(name='ID', primary_key=True)
    name = models.CharField(max_length=50)
    address1 = models.CharField(max_length=70)
    address2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    pincode = models.IntegerField()
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    mobile_number = models.CharField(
        validators=[phone_regex], max_length=13, blank=True)  # validators should be a list
    gst_number = models.CharField(name='GST Number', max_length=50, blank=True)
    agent_commission = models.IntegerField()

    def __str__(self):
        return self.name


class Customer(models.Model):
    #customer_id = models.AutoField(name='ID', primary_key=True)
    name = models.CharField(max_length=50)
    address1 = models.CharField(max_length=70)
    address2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    pincode = models.IntegerField()
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    mobile_number = models.CharField(
        validators=[phone_regex], max_length=13, blank=True)  # validators should be a list
    gst_number = models.CharField(name='GST Number', max_length=50, blank=True)
    max_due_date = models.IntegerField()

    def __str__(self):
        return self.name


class Transport(models.Model):
    #transport_id = models.AutoField(name='ID', primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Bank(models.Model):
    #bank_id = models.AutoField(name='ID', primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PurchaseEntry(models.Model):
    created_on = models.DateField(auto_now_add=True)

    # bill_no = models.CharField(name='Bill No', max_length=20)
    # bill_date = models.DateField(name='Bill date')
    # supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    # goods_val = models.IntegerField(name='Goods Value')
    # discount = models.IntegerField(name='Discount', blank=True, null=True)
    # i_gst_tax = models.IntegerField(name='IGST', blank=True, null=True)
    # c_gst_tax = models.IntegerField(name='CGST', blank=True, null=True)
    # s_gst_tax = models.IntegerField(name='SGST', blank=True, null=True)

    bill_no = models.CharField(max_length=20)
    bill_date = models.DateField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    goods_val = models.IntegerField()
    d_percent = models.IntegerField(blank=True, null=True)
    d_value = models.IntegerField(blank=True, null=True)
    #i_gst_tax = models.IntegerField(blank=True, null=True)
    # c_gst_tax = models.DecimalField(
    #    max_digits=4, decimal_places=2, blank=True, null=True)
    # s_gst_tax = models.DecimalField(
    #    max_digits=4, decimal_places=2, blank=True, null=True)

    transport = models.ForeignKey(Transport, on_delete=models.CASCADE)
    lr_no = models.CharField(max_length=30)
    lr_date = models.DateField()
    fright = models.DecimalField(max_digits=6, decimal_places=2)
    booking_station = models.CharField(max_length=20, blank=True)

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    delivery_date = models.DateField()

    # def __str__(self):
    #     return self.supplier

    class Meta:
            verbose_name_plural = 'Purchase Entries'


class PaymentEntry(models.Model):
    bill_no = models.CharField(max_length=20)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=256, choices=[(
        'cash', 'cash'), ('cheque', 'cheque'), ('NEFT', 'NEFT')])
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    cheque_no = models.CharField(max_length=25)
    amount = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Payment Entries'
