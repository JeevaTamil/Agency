# Generated by Django 2.2.4 on 2020-03-27 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200327_0344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseentry',
            name='c_gst_tax',
        ),
        migrations.RemoveField(
            model_name='purchaseentry',
            name='i_gst_tax',
        ),
        migrations.RemoveField(
            model_name='purchaseentry',
            name='s_gst_tax',
        ),
    ]
