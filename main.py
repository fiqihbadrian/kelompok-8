from ast import While
import pandas as pd

# jasa editing dan desain [type B]


# list
kode_jasa = []
nama_jasa = []
harga_jasa = []
total_harga = []
note = []


# Daftar Harga Jasa Editing dan Desain
print("======================================================")
print("=== DAFTAR JASA EDITING DAN DESAIN ===".center(55))
print("======================================================")
print("Pilihlah jenis jasa yang anda inginkan")
print("------------------------------------------------------")
print("No.   Kode Jasa        Jenis Jasa            Harga")
print("1.        EF          Editing Foto         Rp 50.000")
print("2.        ED          Editing Video        Rp 100.000")
print("3.        DD          Desain Digital       Rp 150.000")
print("4.        DC          Desain Cetak         Rp 200.000")
print("------------------------------------------------------")

# Input jumlah jasa yang ingin dipesan (jika salah ulang lagi)

nama = input("MASUKAN NAMA ANDA: ")

while True:
    try:
        banyak_desain_editing = int(input("MASUKAN JUMLAH JASA YANG INGIN DIPESAN: "))

        if banyak_desain_editing < 1:
            print("Jumlah jasa minimal 1. Silakan coba lagi.")
        else:
            break

    except ValueError:
        print("\033[31m Input harus berupa ANGKA! Silakan coba lagi.\033[0m")
print("-"*54)


# Input kode jasa sesuai jumlah yang diinginkan
for i in range(banyak_desain_editing):
    while True:
        input_kode_jasa = input(f"Masukan kode jasa ke-{i+1} (EF/ED/DD/DC): ").upper()

        if input_kode_jasa == 'EF':
            note.append(input("Masukan notes tambahan untuk Editing Foto (tekan Enter jika tidak ada): "))
            kode_jasa.append(input_kode_jasa)
            nama_jasa.append("Editing Foto")
            harga_jasa.append(50000)
            break


        elif input_kode_jasa == 'ED':
            note.append(input("Masukan notes tambahan untuk Editing Video (tekan Enter jika tidak ada): "))
            kode_jasa.append(input_kode_jasa)
            nama_jasa.append("Editing Video")
            harga_jasa.append(100000)
            break

        elif input_kode_jasa == 'DD':
            note.append(input("Masukan notes tambahan untuk Desain Digital (tekan Enter jika tidak ada): "))
            kode_jasa.append(input_kode_jasa)
            nama_jasa.append("Desain Digital")
            harga_jasa.append(150000)
            break

        elif input_kode_jasa == 'DC':
            note.append(input("Masukan notes tambahan untuk Desain Cetak (tekan Enter jika tidak ada): "))
            kode_jasa.append(input_kode_jasa)
            nama_jasa.append("Desain Cetak")
            harga_jasa.append(200000)
            break

        else:
            print("\033[31m Kode jasa tidak valid! Silakan masukkan EF, ED, DD, atau DC. \033[0m")


    

# Menghitung total harga
for harga in harga_jasa:
    total_harga.append(harga)   
    total = sum(total_harga)


# Tampilan ringkasan pesanan
if kode_jasa:
    print("\n\n")
    print("="*54)
    print("=== RINGKASAN PESANAN ===".center(55))
    print("-" * 54)
    print(f"Nama Pemesan: {nama}")
    print("-" * 54)
    print(f"{'No.':<5}{'Kode Jasa':<15}{'Jenis Jasa':<22}{'Harga':<10}")
    print("-" * 54)


    # Tampilan jasa yang dipesan
    for i in range(len(kode_jasa)):
        print(
            f"{i+1:<5}"
            f"{kode_jasa[i]:<15}"
            f"{nama_jasa[i]:<22}"
            f"Rp {harga_jasa[i]:,.0f}"
        )


    print("-"*54)

    print("Notes Tambahan".center(54))
    print(f"{'Kode Jasa':<12}{'Note'}")
    print(f"{'---------':<12}{'----'}")
    for i in range(len(note)):
        print(
            f"{kode_jasa[i]:<12}"
            f"{note[i]}"
        )

    print("-"*54)


    print(f"Total Harga: Rp {total:,}")
    print("="*54)

    # Proses pembayaran
    while True:
        try:
            pembayaran = int(input("Masukkan jumlah pembayaran (Rp): "))

            if pembayaran < total:
                print("\033[31m Pembayaran tidak cukup! Silakan coba lagi.\033[0m")
            else:
                kembalian = pembayaran - total
                print(f"Pembayaran diterima. Kembalian Anda: Rp {kembalian:,}")
                break
        except ValueError:
            print("\033[31m Input harus berupa ANGKA! Silakan coba lagi.\033[0m")
    print("="*54)
    print("Terima kasih telah menggunakan layanan kami!\npembelian anda akan segera kami proses.")
    print("="*54)
