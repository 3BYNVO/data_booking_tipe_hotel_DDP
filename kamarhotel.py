def booking_hotel(jenis_kamar, check_in, check_out):
    if jenis_kamar == "Standard":
        tarif = 200000
    elif jenis_kamar == "Deluxe":
        tarif = 350000
    else:
        print("Tipe Kamar Tidak Tersedia untuk saat ini")
        return

    durasi_bermalam = check_out - check_in
    biaya = tarif * durasi_bermalam

    print("==== DATA PEMESANAN HOTEL ANDA ===")
    print("Jenis Kamar          :", jenis_kamar)
    print("Tanggal Check-in     :", check_in)
    print("Tanggal Check-out    :",check_out)
    print("Durasi               :", durasi_bermalam, "malam")
    print("Total Biaya Anda     : Rp", biaya)

    return biaya

jenis_kamar = input("Masukkan Tipe Kamar anda (Standard/Deluxe) : ")
check_in = int (input("Masukkan Tanggal anda Check-in  : "))
check_out = int (input("Masukkan Tanggal anda Check-out : "))

booking_hotel (jenis_kamar, check_in, check_out)