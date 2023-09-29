from django.shortcuts import render, redirect
from . import models
from datetime import datetime
import calendar
from .decorators import role_required
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login , logout, authenticate
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.forms import DateInput
from django.db import transaction
from django.core.exceptions import ValidationError
import json
# from weasyprint import HTML
from django.template.loader import render_to_string
import tempfile

# done Progress : BAL, produk, penjualan, pembelian
# on-going Progress : Detail Penjualan, Detail Pembelian, Detail BAL (update)

# Create your views here.
komoditas_to_produk_mapping = {
        'BAL Jaket Sangat Baik': ('Jaket SB', 0.4),
        'BAL Jaket Baik': ('Jaket B', 0.3),
        'BAL Jaket Cukup Baik': ('Jaket CB', 0.2),
        'BAL Kemeja Sangat Baik': ('Kemeja SB', 0.45),
        'BAL Kemeja Baik': ('Kemeja B', 0.35),
        'BAL Kemeja Cukup Baik': ('Kemeja CB', 0.25),
    }

#  LOGIN
@login_required(login_url="login")
def logoutview(request):
    logout(request)
    messages.info(request,"Berhasil Logout")
    return redirect('login')

def loginview(request):
    if request.user.is_authenticated:
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'karyawan':
            return redirect('mitra')
        elif group in ['admin', 'owner']:
            return redirect('home')
    else:
        return render(request,"login.html")

def performlogin(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed")
    else:
        username_login = request.POST['username']
        password_login = request.POST['password']
        userobj = authenticate(request, username=username_login,password=password_login)
        if userobj is not None:
            login(request, userobj)
            messages.success(request,"Login success")
            if userobj.groups.filter(name='admin').exists() or userobj.groups.filter(name='owner').exists():
                return redirect("home")
            elif userobj.groups.filter(name='karyawan').exists():
                return redirect("mitra")
            
        else:
            messages.error(request,"Username atau Password salah !!!")
            return redirect("login")
        
@login_required(login_url="login")
def performlogout(request):
    logout(request)
    return redirect("login")

def home(request):
    return HttpResponse("Anda Berhasil Login")

# DASHBOARD 
@login_required(login_url="login")
@role_required(["owner", 'admin'])

def home(request):
    return HttpResponse("Anda Berhasil Login")

# PRODUK

@login_required(login_url="login")
@role_required(["owner", 'admin'])
def produk(request):
    allprodukobj = models.produk.objects.all()

    return render (request, 'produk/produk.html',{
        'allprodukobj' : allprodukobj,
        })

@login_required(login_url="login")
@role_required(["owner", 'admin'])
def create_produk(request):
    if request.method == "GET" :
        return render(request, 'produk/createproduk.html', )
    else:
        nama_produk = request.POST['namaproduk']
        kualitas_produk = request.POST['kualitasproduk']
        kategori_produk = request.POST['kategoriproduk']
        harga_produk = request.POST['hargaproduk']

        models.produk(
            namaproduk = nama_produk,
            kualitas_produk = kualitas_produk,
            kategori_produk = kategori_produk,
            hargaproduk = harga_produk,
        ).save()
        return redirect('produk')


@login_required(login_url="login")
@role_required(["owner", 'admin'])
def update_produk(request,id):
    produkobj = models.produk.objects.get(id_produk=id)
    if request.method == "GET":
        return render(request, 'produk/updateproduk.html', {
            'produkobj' : produkobj
            })
    else:
        produkobj.namaproduk = request.POST['namaproduk']
        produkobj.kualitasproduk = request.POST['kualitasproduk']
        produkobj.kategori_produk = request.POST['kategoriproduk']
        produkobj.hargaproduk= request.POST['hargaproduk']
        produkobj.save()
        return redirect('produk')

@login_required(login_url="login")
@role_required(["owner"])
def delete_produk(request, id):
    produkobj = models.produk.objects.get(id_produk=id)
    produkobj.delete()
    return redirect('produk')

# BAL

@login_required(login_url="login")
@role_required(["owner", 'admin'])
def BAL(request):
    allBALobj = models.BAL.objects.all()

    return render (request, 'BAL/BAL.html',{
        'allBALobj' : allBALobj,
        })

@login_required(login_url="login")
@role_required(["owner", 'admin'])
def create_BAL(request):
    if request.method == "GET" :
        return render(request, 'BAL/createBAL.html', )
    else:
        kode_BAL = request.POST['kodeBAL']
        kapasitas_BAL = request.POST['kapasitasBAL']
        harga_BAL = request.POST['hargaBAL']

        models.BAL(
            kode_BAL = kode_BAL,
            kapasitas_BAL = kapasitas_BAL,
            hargaBAL = harga_BAL,
        ).save()
        return redirect('BAL')


@login_required(login_url="login")
@role_required(["owner", 'admin'])
def update_BAL(request,id):
    BALobj = models.BAL.objects.get(id_BAL=id)
    if request.method == "GET":
        return render(request, 'BAL/updateBAL.html', {
            'BALobj' : BALobj
            })
    else:
        BALobj.kode_BAL = request.POST['kodeBAL']
        BALobj.kapasitas_BAL = request.POST['kapasitasBAL']
        BALobj.harga_BAL = request.POST['hargaBAL']
        BALobj.save()
        return redirect('BAL')

@login_required(login_url="login")
@role_required(["owner"])
def delete_BAL(request, id):
    BALobj = models.BAL.objects.get(id_BAL=id)
    BALobj.delete()
    return redirect('BAL')

# DETAIL BAL

@login_required(login_url="login")
@role_required(["owner", 'admin', 'karyawan'])
def detailBAL(request):
    alldetailBALobj = models.detailBAL.objects.all()
    detailBAL_pilah = models.detailBAL.objects.filter(id_BAL__kode_bal = "Pilah")
    return render(request, 'detailBAL/detailBAL.html', {
        "alldetailBALobj" : alldetailBALobj,
        'detailBAL_pilah' : detailBAL_pilah
        })

@login_required(login_url="login")
@role_required(["owner", 'karyawan'])
def update_detailBAL(request, id):
    detailBALobj = models.detailBAL.objects.get(id_detailpanen=id)
    allprodukobj = models.produk.objects.all()
    allBALobj = models.BAL.objects.all()

    if request.method == "GET":
        return render(request, 'detailBAL/updatedetailBAL.html', {
            'allddetailBAL': detailBALobj,
            'dataproduk' : allprodukobj,
            'dataBAL' : allBALobj
        })
    elif request.method == "POST":
        id_produk = request.POST["id_produk"]
        getidproduk = models.produk.objects.get(id_produk=id_produk)

        id_BAL = request.POST["id_BAL"]
        getidBAL = models.produk.objects.get(id_BAL=id_BAL)

        jumlahproduk = request.POST["jumlahproduk"]

        detailBALobj.id_produk = getidproduk
        detailBALobj.id_BAL = getidBAL
        detailBALobj.jumlahproduk = jumlahproduk
        detailBALobj.save()

        return redirect('detailBAl')


@login_required(login_url="login")
@role_required(["owner"])
def delete_detailBAL(request,id):
    detailBALobj = models.detailBAL.objects.get(id_detailBAL=id)
    detailBALobj.delete()
    return redirect('detailBAL')

# PENJUALAN 

@login_required(login_url="login")
@role_required(["owner", 'admin'])
def penjualan(request):
    penjualanobj = models.penjualan.objects.all()
    return render (request, 'penjualan.html',{
        'penjualanobj' : penjualanobj
    })

@login_required(login_url="login")
@role_required(["owner", 'admin'])
def create_penjualan(request):
    if request.method == "GET" :
        return render(request, 'penjualan/createpenjualan.html', )
    else:
        tanggal_penjualan = request.POST['tanggal_penjualan']
        jumlah_penjualan = request.POST['jumlahpenjualan']

        models.penjualan(
            tanggal_penjualan = tanggal_penjualan,
            jumlah_penjualan = jumlah_penjualan,
        ).save()
        return redirect('BAL')

@login_required(login_url="login")
@role_required(["owner", 'admin'])
def updatepenjualan(request,id):
    penjualanobj = models.penjualan.objects.get(id_penjualan=id)
    if request.method == "GET":
        tanggal_penjualan = datetime.strftime(penjualanobj.tanggal_penjualan, '%Y-%m-%d')
        return render(request, 'updatepenjualan.html', {
            'penjualanobj' : penjualanobj,
            'tanggal_penjualan' : tanggal_penjualan,
        })
    else:
        tanggal_penjualan = request.POST['tanggal_penjualan']

        penjualanobj.jumlah_penjualan = request.POST['jumlahpenjualan']
        penjualanobj.tanggal_penjualan = tanggal_penjualan
        penjualanobj.save()

        return redirect('penjualan')

@login_required(login_url="login")
@role_required(["owner"])
def deletepenjualan(request, id):
    penjualanobj = models.penjualan.objects.get(id_penjualan = id)
    penjualanobj.delete()
    return redirect ('penjualan')

# DETAIL PENJUALAN

@login_required(login_url="login")
@role_required(["owner", 'admin'])
def adddetailpenjualan(request, id):
    OrderFormSet = inlineformset_factory(models.penjualan, models.detailPenjualan, fields = ('idproduk', 'jumlahBAL', ))
    penjualan = models.penjualan.objects.get(idpenjualan = id)
    formset = OrderFormSet (instance = penjualan)
    if request.method == 'POST' :
        formset = OrderFormSet (request.POST, instance = penjualan)
        if formset.is_valid():
            formset.save()
            return redirect('penjualan')
    context = {'formest' : formset}

# PEMBELIAN 

@login_required(login_url="login")
@role_required(["owner", 'admin'])
def pembelian(request):
    pembelianobj = models.pembelian.objects.all()
    return render (request, 'pembelian.html',{
        'pembelianobj' : pembelianobj
    })

@login_required(login_url="login")
@role_required(["owner", 'admin'])
def create_pembelian(request):
    if request.method == "GET" :
        return render(request, 'pembelian/createpembelian.html', )
    else:
        tanggal_pembelian = request.POST['tanggal_pembelian']
        jumlah_pembelian = request.POST['jumlahpembelian']

        models.pembelian(
            tanggal_pembelian = tanggal_pembelian,
            jumlah_pembelian = jumlah_pembelian,
        ).save()
        return redirect('BAL')

@login_required(login_url="login")
@role_required(["owner", 'admin'])
def updatepembelian(request,id):
    pembelianobj = models.pembelian.objects.get(id_pembelian=id)

    if request.method == "GET":
        tanggal = datetime.strftime(pembelianobj.tanggal_pembelian, '%Y-%m-%d')
        return render(request, 'updatepembelian.html', {
            'pembelianobj' : pembelianobj,
            'tanggal' : tanggal,
        })
    else:
        tanggal_pembelian = request.POST['tanggal_pembelian']

        pembelianobj.jumlah_pembelian = request.POST['jumlahpembelian']
        pembelianobj.tanggal_pembelian = tanggal_pembelian
        pembelianobj.save()

        return redirect('pembelian')

@login_required(login_url="login")
@role_required(["owner"])
def deletepembelian(request, id):
    pembelianobj = models.pembelian.objects.get(id_pembelian = id)
    pembelianobj.delete()
    return redirect ('pembelian')

# DETAIL PEMBELIAN

@login_required(login_url="login")
@role_required(["owner", 'admin'])
def adddetailpembelian(request, id):
    OrderFormSet = inlineformset_factory(models.pembelian, models.detailPembelian, fields = ('idBAL', 'jumlahBAL', ))
    pembelian = models.pembelian.objects.get(idpembelian = id)
    formset = OrderFormSet (instance = pembelian)
    if request.method == 'POST' :
        formset = OrderFormSet (request.POST, instance = pembelian)
        if formset.is_valid():
            formset.save()
            return redirect('pembalian')
    context = {'formest' : formset}
