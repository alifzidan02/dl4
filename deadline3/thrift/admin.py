from django.contrib import admin
from . import models

admin.site.register(models.pembelian)
admin.site.register(models.penjualan)
admin.site.register(models.BAL)
admin.site.register(models.produk)
admin.site.register(models.detailPembelian)
admin.site.register(models.detailPenjualan)
admin.site.register(models.detailBAL)

# Register your models here.
