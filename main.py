# jasa editing dan desain [type B]


# Modul
import pandas as pd


# kode warna
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[0m'


# list
kode_jasa = []
nama_jasa = []
harga_jasa = []
total_harga = []
note = []


# Daftar Harga Jasa Editing dan Desain
print("="*54)
print(f"{GREEN}DAFTAR JASA EDITING DAN DESAIN{RESET}".center(63))
print("="*54)
print("Pilihlah jenis jasa yang anda inginkan")
print("-"*54)
print("No.   Kode Jasa        Jenis Jasa            Harga")
print("-"*54)
print("1.        EF          Editing Foto         Rp 100.000")
print("2.        ED          Editing Video        Rp 200.000")
print("3.        DD          Desain Digital       Rp 150.000")
print("4.        DC          Desain Cetak         Rp 200.000")
print("-"*54)


# Input data diri
print("\n")
print("Sebelum memesan, silakan masukkan data diri anda terlebih dahulu.")
nama = input("MASUKAN NAMA ANDA: ")
notelp = input("MASUKAN NO TELEPON ANDA: ")


# fungsi while (jika salah ulangi lagi)
while True:
    try:
        # Input berapa banyak yang ingin di pesan
        banyak_desain_editing = int(input("MASUKAN JUMLAH JASA YANG INGIN DIPESAN: "))

        if banyak_desain_editing < 1:
            print("Jumlah jasa minimal 1. Silakan coba lagi.")
        else:
            break

    except ValueError:
        print(f"{RED}Input harus berupa ANGKA! Silakan coba lagi.{RESET}")
print("-"*54)


# Percebangan
for i in range(banyak_desain_editing):
    while True:
        input_kode_jasa = input(f"Masukan kode jasa ke-{i+1} (EF/ED/DD/DC): ").upper()

        if input_kode_jasa == 'EF':
            note.append(input("Masukan notes tambahan untuk Editing Foto (tekan Enter jika tidak ada): "))
            kode_jasa.append(input_kode_jasa)
            nama_jasa.append("Editing Foto")
            harga_jasa.append(100000)
            break


        elif input_kode_jasa == 'ED':
            note.append(input("Masukan notes tambahan untuk Editing Video (tekan Enter jika tidak ada): "))
            kode_jasa.append(input_kode_jasa)
            nama_jasa.append("Editing Video")
            harga_jasa.append(200000)
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
            print(f"{RED}Kode jasa tidak valid! Silakan masukkan EF, ED, DD, atau DC.{RESET}")


# Menghitung total harga aritmatika
for harga in harga_jasa:
    total_harga.append(harga)
    total = sum(total_harga)


# Tampilan ringkasan pesanan
if kode_jasa:
    print("\n\n")
    print("="*54)
    print(f"{GREEN}RINGKASAN PESANAN{RESET}".center(63))
    print("-" * 54)
    print(f"Nama Pemesan: {nama}")
    print(f"No. Telepon : {notelp}")


    # Header Table
    print("-" * 54)
    print(
    f"{' ':<2}"
    f"{'No.':<8}"
    f"{'Kode Jasa':<18}"
    f"{'Jenis Jasa':<19}"
    f"{'Harga':<14}"
    )
    print("-" * 54)


    # Tampilan jasa yang dipesan (list pandas)
    df = pd.DataFrame({
        "No.": range(1, len(kode_jasa) + 1),
        "Kode Jasa": kode_jasa,
        "Jenis Jasa": nama_jasa,
        "Harga": harga_jasa
    })

    
    # mengatur list pandas (jelasin apa itu index kenapa header di falsekan)
    print(
    df.to_string(
        index=False,
        header=False,
        col_space={
            "No.": 4,
            "Kode Jasa": 11,
            "Jenis Jasa": 21,
            "Harga": 15
        },
        formatters={
            "Harga": lambda x: f"Rp {x:,.0f}".replace(",", ".")
        }
        )
    )


    print("-"*54)
    print(f"{YELLOW}Notes Tambahan{RESET}".center(63))
    print(f"{'Kode Jasa':<12}{'Note'}")
    print(f"{'---------':<12}{'----'}")


    # percabangan untuk catatan
    for i in range(len(note)):
        if note[i] == '':
            print(
                f"{kode_jasa[i]:<12}"
                f"{RED}Tidak ada note{RESET}"
            )
        else:
            print(
                f"{kode_jasa[i]:<12}"
                f"{note[i]}"
            )


    print("-"*54)
    print(f"Total Harga: Rp {total:,}")
    print("="*54)


    # Proses pembayaran dan kembalian
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
