# Generated by Django 4.2.5 on 2023-09-20 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BAL',
            fields=[
                ('id_BAL', models.AutoField(primary_key=True, serialize=False)),
                ('kodeBAL', models.PositiveIntegerField()),
                ('kapasitas', models.PositiveBigIntegerField()),
                ('hargaBAL', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='pembelian',
            fields=[
                ('id_pembelian', models.AutoField(primary_key=True, serialize=False)),
                ('TanggalPembelian', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='penjualan',
            fields=[
                ('id_penjualan', models.AutoField(primary_key=True, serialize=False)),
                ('tanggalPenjualan', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='produk',
            fields=[
                ('id_produk', models.AutoField(primary_key=True, serialize=False)),
                ('kualitas', models.CharField(max_length=50)),
                ('nama_produk', models.CharField(max_length=50)),
                ('kategori', models.CharField(max_length=50)),
                ('harga_jual', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='detailPenjualan',
            fields=[
                ('id_detailPenjualan', models.AutoField(primary_key=True, serialize=False)),
                ('id_penjualan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thrift.penjualan')),
                ('id_produk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thrift.produk')),
            ],
        ),
        migrations.CreateModel(
            name='detailPembelian',
            fields=[
                ('id_detailPembelian', models.AutoField(primary_key=True, serialize=False)),
                ('id_BAL', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thrift.bal')),
                ('id_pembelian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thrift.pembelian')),
            ],
        ),
        migrations.CreateModel(
            name='detailBAL',
            fields=[
                ('id_detailBAL', models.AutoField(primary_key=True, serialize=False)),
                ('jumlahproduk', models.PositiveBigIntegerField()),
                ('id_BAL', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thrift.bal')),
                ('id_produk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thrift.produk')),
            ],
        ),
    ]