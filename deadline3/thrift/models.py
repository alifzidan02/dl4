from django.db import models

class produk(models.Model):
    id_produk = models.AutoField(primary_key=True)
    kualitas = models.CharField(max_length=50)
    nama_produk = models.CharField(max_length=50)
    kategori = models.CharField(max_length=50)
    harga_jual = models.IntegerField()

    def __str__(self) :
        return str(self.nama_produk)
    
class pembelian(models.Model):
    id_pembelian = models.AutoField(primary_key=True)
    TanggalPembelian = models.DateField()

    def __str__(self) :
        return '{}'.format(self.TanggalPembelian)
    
class penjualan(models.Model):
    id_penjualan = models.AutoField(primary_key=True)
    tanggalPenjualan = models.DateField()

    def __str__(self) :
        return '{}'.format(self.tanggalPenjualan)
    
class BAL(models.Model):
    id_BAL = models.AutoField(primary_key=True)
    kodeBAL = models.CharField(max_length=50)
    kapasitas = models.PositiveBigIntegerField()
    hargaBAL = models.IntegerField()

    def __str__(self) :
        return '{}'.format(self.kodeBAL)

class detailPembelian(models.Model):
    id_detailPembelian = models.AutoField(primary_key=True)
    id_pembelian = models.ForeignKey(pembelian, on_delete=models.CASCADE)
    id_BAL = models.ForeignKey(BAL, on_delete=models.CASCADE)
    jumlah = models.IntegerField()

    def __str__(self) :
        return '{} - {} - {}'.format(self.id_pembelian, self.id_BAL, self.jumlah)

class detailPenjualan(models.Model):
    id_detailPenjualan = models.AutoField(primary_key=True)
    id_produk = models.ForeignKey(produk, on_delete=models.CASCADE)
    id_penjualan = models.ForeignKey(penjualan, on_delete=models.CASCADE)
    jumlah= models.IntegerField()

    def __str__(self) :
        return '{} - {} - {}'.format(self.id_produk,self.id_penjualan, self.jumlah)
    
class detailBAL(models.Model):
    id_detailBAL = models.AutoField(primary_key=True)
    id_BAL = models.ForeignKey(BAL, on_delete=models.CASCADE)
    id_produk = models.ForeignKey(produk, on_delete=models.CASCADE)
    jumlahproduk = models.PositiveBigIntegerField()

    def __str__(self) :
        return '{} - {} - {}'.format(self.id_detailBAL, self.id_BAL,self.id_produk)

# Create your models here.
