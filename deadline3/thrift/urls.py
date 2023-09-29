from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home, name="home"),

    # LOGIN
    path('',views.loginview, name='login'),
    path('performlogin',views.performlogin,name="performlogin"),
    path('performlogout',views.performlogout,name="performlogout"),

    # PRODUK
    path('produk/', views.produk,name='produk'),
    path('produk/createproduk', views.create_produk,name='createproduk'),
    path('produk/updateproduk/<str:id>', views.update_produk,name='updateproduk'),
    path('deleteproduk/<str:id>', views.delete_produk,name='deleteproduk'),

    # BAL
    path('BAL/', views.BAL,name='BAL'),
    path('BAL/createBAL', views.create_BAL,name='createBAL'),
    path('BAL/updateBAL/<str:id>', views.update_BAL,name='updateBAL'),
    path('deleteBAL/<str:id>', views.delete_BAL,name='deleteBAL'),

    # PENJUALAN
    path('penjualan/', views.penjualan,name='penjualan'),
    path('penjualan/createpenjualan', views.create_penjualan,name='createpenjualan'),
    path('penjualan/updatepenjualan/<str:id>', views.updatepenjualan,name='updatepenjualan'),
    path('deletepenjualan/<str:id>', views.deletepenjualan,name='deletepenjualan'),

    # PEMBELIAN
    path('pembelian/', views.pembelian,name='pembelian'),
    path('pembelian/createpembelian', views.create_pembelian,name='createpembelian'),
    path('pembelian/updatepembelian/<str:id>', views.updatepembelian,name='updatepembelian'),
    path('deletepembelian/<str:id>', views.deletepembelian,name='deletepembelian'),

    # # DETAIL PENJUALAN
    # path('detailpenjualan', views.detail_penjualan,name='detailpenjualan'),
    # path('detailpenjualan1', views.detail_penjualan_komoditas,name='detailpenjualan_komoditas'),
    # path('detailpenjualan2', views.detail_penjualan_produk,name='detailpenjualan_produk'),
    # path('detailpenjualan/createdetailpenjualan_produk/<int:id>/', views.create_detailpenjualan_produk, name='createdetailpenjualan_produk'),
    # path('detailpenjualan/createdetailpenjualan_komoditas/<int:id>/', views.create_detailpenjualan_komoditas, name='createdetailpenjualan_komoditas'),
    # path('detailpenjualan/updatedetailpenjualan/<str:id>', views.update_detailpenjualan,name='updatedetailpenjualan'),
    # path('deletedetailpenjualan/<str:id>', views.delete_detailpenjualan,name='deletedetailpenjualan'),

    # # DETAIL PEMBELIAN
    # path('panen/', views.panen,name='panen'),
    # path('panen/updatepanen/<str:id>', views.update_panen,name='updatepanen'),
    # path('deletepanen/<str:id>', views.delete_panen,name='deletepanen'),

    # # DETAIL BAL
    # path('detailpanen/', views.detailpanen,name='detailpanen'),
    # path('panen/createpanen/<str:id>/', views.create_panen,name='createpanen'),
    # path('detailpanen/ubahdetailpanen/<str:id>/', views.ubah_panen,name='ubahdetailpanen'),
    # path('detailpanen/updatedetailpanen/<str:id>', views.update_detailpanen,name='updatedetailpanen'),
    # path('deletedetailpanen/<str:id>', views.delete_detailpanen,name='deletedetailpanen'),

    # # LAPORAN
    # path('laporan', views.laporan_laba_rugi, name='laporan'),
    # path('laporanpdf/<str:mulai>/<str:akhir>',views.laporan_laba_rugi_pdf,name='laporanpdf'),
    # path('laporanjual', views.laporanpenjualan, name='laporanjual'),
    # path('laporanpenjualanpdf/<str:mulai>/<str:akhir>',views.laporanpenjualanpdf,name='laporanpenjualanpdf'),
    # path('laporanpanen', views.laporanpanen,name='laporanpanen'),
    # path('laporanpanenpdf/<str:mulai>/<str:akhir>',views.laporanpanenpdf,name='laporanpanenpdf'),

    
    ]