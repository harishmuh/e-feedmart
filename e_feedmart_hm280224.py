# Melakukan import library Tabulate
from tabulate import tabulate 

# Mendesain head_items sebagai komponen tampilan menu tabulate
head_items = ["Kode Produk", "Produk", "Produsen", "Deskripsi", "Stock", "Harga"]

# Daftar produk pakan 
list_items = [
    ["8882", "Pakan ikan 'Bintang'", "PT. CPP", "Protein 31%, Lemak 5%", 30, 567498],
    ["PROFISH3", "Pakan ikan mas", "PT. Cargill", "Protein 28%", 40, 517498],
    ["SNA12", "Pakan ikan terapung", "PT. Sinta Prima", "Protein 33%, Lemak 5%", 25, 398999],
    ["SPLA12", "Pakan apung lele", "PT. Suri Tani Pemuka", "Protein 32%", 50, 391200]
]

# Isi list welcoming atau user menu
welcoming_menu = [
    ["Selamat datang di e-Feed Mart!!"],
    ["Pilih posisi anda?"],
    ["1. Penjual Pakan Ikan\n2. Pembudidaya/Pembeli Pakan Ikan\n3. Stop Program"]
]

# Isi list menu untuk user merchant atau penjual
feed_merchant_menu = [
    ["Selamat datang di e-Feed Mart!!"],
    ["Sebagai Seller, apa yang ingin anda lakukan?"],
    ["1. Menampilkan daftar produk\n2. Menambah stok produk pakan\n3. Melakukan update stok pakan\n4. Menghapus data stok pakan\n5. Kembali ke menu awal"]
]

# Isi list menu untuk user customer atau pembeli
feed_customer_menu = [
    ["Selamat datang di e-Feed Mart!!"],
    ["Sebagai pembeli, apa yang ingin anda lakukan?"],
    ["1. Melihat daftar produk pakan\n2. Membeli produk pakan\n3. Kembali ke menu awal"]
]

# Isi list menu 1 user merchant/penjual
menu_1_index = [
    ["Pilih lah menu di bawah ini"],
    ["1. Menampilkan semua daftar produk pakan\n2. Menampilkan produk sesuai kode produk\n3. Menampilkan produk dari harga termurah\n4. Menampilkan produk dari harga tertinggi\n5. Kembali ke menu sebelumnya"]
]

# Isi list menu 2 user merchant/penjual
menu_2_index = [
    ["Pilih lah menu di bawah ini"],
    ["1. Menambahkan produk pakan baru\n2. Kembali ke menu sebelumnya"]
]

# Isi list menu 3 merchant/penjual
menu_3_index = [
    ["Pilih lah menu di bawah ini"],
    ["1. Melakukan pengubahan daftar pakan\n2. Kembali ke menu sebelumnya"]
]

# Isi list menu 4 merchant/penjual
menu_4_index = [
    ["Pilih lah menu di bawah ini"],
    ["1. Melakukan penghapusan produk pakan tertentu\n2. Melakukan penghapusan semua produk pakan\n3. Kembali ke menu sebelumnya"]
]

# Mendesain fungsi-fungsi menu dan sub-menu dari komponen aplikasi

# Fungsi menampilkan seluruh daftar produk pakan
def display_items():
    print(tabulate(list_items, headers=head_items, tablefmt="fancy_grid"))

# Fungsi menampilkan pilihan menu utama untuk memilih peran sebagai penjual atau pembeli, serta exit program
def display_user_menu():
    print(tabulate(welcoming_menu, tablefmt="fancy_grid"))

# Fungsi menampilkan pilihan sub menu pada user penjual
def display_seller_menu():
    print(tabulate(feed_merchant_menu, tablefmt="fancy_grid"))

# Fungsi menampilkan pilihan sub menu pada user pembeli
def display_customer_menu():
    print(tabulate(feed_customer_menu, tablefmt="fancy_grid"))

# Fungsi menampilkan pilihan sub menu untuk menampilkan daftar produk pakan
def menu_1_display():
    print(tabulate(menu_1_index, tablefmt="fancy_grid"))

# Fungsi menampilkan pilihan sub menu untuk menambahkan produk pakan
def menu_2_display():
    print(tabulate(menu_2_index, tablefmt="fancy_grid"))

# Fungsi menampilkan pilihan sub menu untuk mengubah/meng-update produk pakan
def menu_3_display():
    print(tabulate(menu_3_index, tablefmt="fancy_grid"))

# Fungsi menampilkan pilihan sub menu untuk menghapus produk pakan
def menu_4_display():
    print(tabulate(menu_4_index, tablefmt="fancy_grid"))

# Fungsi melakukan pengurutan berdasarkan harga termurah hingga termahal
def sort_by_price_asc(products):
    return sorted(products, key= lambda x: x[5])

# Fungsi melakukan pengurutan berdasarkan harga termahal hingga termurah
def sort_by_price_desc(products):
    return sorted(products, key= lambda x: x[5], reverse=True)


# Fungsi menjalankan aplikasi dalam pemilihan user
def program():        
    while True:
        display_user_menu()
        user_menu_input = input('Mohon pilih angka menu yang ingin dijalankan: ')
        # Input '1' untuk memilih peran sebagai merchant atau penjual
        if user_menu_input == '1':
            feed_seller()
        # Input '2' untuk memilih peran sebagai customer atau pembeli pakan
        elif user_menu_input == '2':
            feed_customer()
        # Input '3' untuk menghentikan atau keluar dari program 
        elif user_menu_input == '3':
            print('Terima kasih dan sampai jumpa!')
            break
        else:
            print('Mohon masukkan input yang benar!')

# Fungsi sebagai merchant atau penjual produk pakan
def feed_seller():
    while True:
        display_seller_menu()
        seller_menu_input = input(f"Masukkan angka menu yang ingin dijalankan: ")
        if seller_menu_input == '1':
            menu_1()
        elif seller_menu_input == '2':
            menu_2()
        elif seller_menu_input == '3':
            menu_3()
        elif seller_menu_input == '4':
            menu_4()
        elif seller_menu_input == '5':
            print("Terima kasih dan sampai jumpa!")
            break
        else:
            print('Mohon masukkan input menu dengan benar!')

# Fungsi seller untuk menampilkan daftar produk pakan
# Terdapat 3 pilihan input: '1' Menampilkan semua daftar produk, '2' Menampilkan produk tertentu, '3' untuk menampilkan produk pakan berdasarkan harga terendah, '4' untuk menampilkan produk pakan berdasarkan harga teringgi '5' Kembali ke menu sebelumnya  
def menu_1():
    if list_items == []:
        print('Daftar produk kosong!')
        return
    while True:
        menu_1_display()
        menu_input_1 = input('Masukkan angka menu yang anda inginkan (1/2/3/4/5): ')
        # Input '1' untuk menampilkan semua daftar produk pakan
        if menu_input_1 == '1':
            display_items()
        # Input '2' untuk menampilkan produk pakan tertentu
        elif menu_input_1 == '2':
            kode_pakan_input = input('Masukkan kode produk pakan yang diinginkan: ').upper()
            for item in list_items:
                if item[0] == kode_pakan_input:
                    print(tabulate([item], headers=head_items, tablefmt="fancy_grid"))
                    break
            else:
                print("Kode produk tidak ditemukan!")
        # Input '3' untuk menampilkan produk pakan berdasarkan harga terrendah
        elif menu_input_1 == '3':
            print("Daftar produk setelah diurutkan berdasarkan harga:")
            sorted_produk_murah = sort_by_price_asc(list_items)
            print(tabulate(sorted_produk_murah, headers=head_items, tablefmt="fancy_grid"))
        # Input '4' untuk menampilkan produk pakan berdasarkan harga tertinggi
        elif menu_input_1 == '4':
            print("Daftar produk setelah diurutkan berdasarkan harga:")
            sorted_produk_mahal = sort_by_price_desc(list_items)
            print(tabulate(sorted_produk_mahal, headers=head_items, tablefmt="fancy_grid"))
        # Input '5' Kembali ke menu sebelumnya
        elif menu_input_1 == '5':
            break
        else:
            print('Mohon masukkan input menu dengan benar!')

# Fungsi seller untuk menambah produk ke daftar produk pakan
# Terdapat pilihan input: '1' untuk menambah produk pakan baru, '2' untuk kembali ke menu sebelumnya  
def menu_2():
    while True:
        menu_2_display()
        display_items()
        menu_input_2 = input('Masukkan angka menu yang anda inginkan (1/2): ')
        # Input '1' untuk menambah produk pakan
        if menu_input_2 == "1":
            while True:
                kode_produk_baru = input("Masukkan kode produk baru: ").upper()
                # Memeriksa apakah kode produk sudah ada dalam daftar
                produk_sudah_ada = False
                for item in list_items:
                    # Jika kode produk sudah ada dalam daftar, maka akan menampilkan notifikasi bahwa produk sudah terdaftar
                    if item[0] == kode_produk_baru:
                        print("Produk sudah terdaftar! Masukkan kode produk yang lain")
                        produk_sudah_ada = True
                        break
                if not produk_sudah_ada:
                    break  # Jika produk belum terdaftar, keluar dari loop
            if not produk_sudah_ada:
                while True:
                    nama_produk_baru = input("Masukkan nama produk baru: ")
                    if not nama_produk_baru.isdigit():
                        break
                    else:
                        print("Nama produk harus mengandung huruf!")
                while True:
                    produsen_baru = input("Masukkan nama produsen baru: ")
                    if not produsen_baru.isdigit():
                        break
                    else:
                        print("Nama produsen harus mengandung huruf!")
                while True:
                    deskripsi_produk_baru = input("Masukkan deskripsi produk baru: ")
                    if not deskripsi_produk_baru.isdigit():
                        break
                    else:
                        print("Deskripsi produk harus mengandung huruf!")
                while True:
                    while True:
                        stock_produk_baru = input("Masukkan jumlah stok produk baru: ")
                        if stock_produk_baru.isdigit() == False or int(stock_produk_baru)<0:
                            print("Masukkan input yang valid!")
                        else:
                            stock_produk_baru = int(stock_produk_baru)
                            break
                    while True:    
                        harga_produk_baru = input("Masukkan harga produk baru: ")
                        if harga_produk_baru.isdigit() == False or int(harga_produk_baru) <= 0:
                            print("Masukkan input yang valid!")
                        else:    
                            harga_produk_baru = int(harga_produk_baru)
                            break
                    break
                while True:
                    checker = input("Apakah anda yakin menyimpan produk ini? (Y/N)").upper()
                    if checker == 'Y':
                        list_items.append([kode_produk_baru, nama_produk_baru, produsen_baru, deskripsi_produk_baru, stock_produk_baru, harga_produk_baru])
                        print(f"Data Anda berupa {nama_produk_baru} dengan kode {kode_produk_baru} dengan kuantitas {stock_produk_baru} telah tersimpan")
                        break
                    elif checker == 'N':
                        menu_2_display()
                        break
                    else:
                        print("Anda memasukkan input yang salah")
                        continue
        elif menu_input_2 == "2":
            display_user_menu()
            break  
        else:
            print()
            print('Mohon masukkan input menu dengan benar!')
            continue


# Fungsi seller untuk mengubah ke daftar produk pakan
# Terdapat pilihan input: '1' untuk melakukan update atau mengubah data dari daftar produk, '2' untuk kembali ke menu sebelumnya 
def menu_3():
    if list_items == []:
        print('Daftar produk kosong!')
        return
    while True:
        menu_3_display()
        display_items()
        menu_input_3 = input('Masukkan angka menu yang anda inginkan (1/2): ')
        # Input '1' untuk mengubah data dari daftar produk pakan
        if menu_input_3 == '1':
            kode_produk_update = input('Masukkan kode produk yang ingin anda ubah :').upper()
           # Mencari indeks produk yang akan diubah
            index_to_update = None
            for i, item in enumerate(list_items):
                if item[0] == kode_produk_update:
                    index_to_update = i
                    break
            if index_to_update is not None:
                column_to_update = input("Ketikkan nama kolom yang ingin anda ubah: ").capitalize()
                if column_to_update in head_items:
                    new_value = input(f"Masukkan nilai baru untuk kolom '{column_to_update}': ")
                    # Validasi untuk kolom 'Stock' dan 'Harga'
                    if column_to_update == 'Stock' or column_to_update == 'Harga':
                        try:
                            new_value = int(new_value)
                            if new_value <= 0:
                                print("Input harus lebih besar dari nol!")
                                continue
                        except ValueError:
                            print("Masukkan angka yang valid!")
                            continue
                    # Validasi khusus untuk kolom 'Produk', 'Deskripsi', dan 'Produsen
                    elif column_to_update == 'Produk' or column_to_update == 'Deskripsi' or column_to_update == 'Produsen':
                        if new_value.isdigit():
                            print("Produk tidak boleh hanya berisi angka saja!")
                            continue
                    while True:    
                        checker = input("Apakah anda yakin akan melakukan pengubahan data? (Y/N)").upper()
                        if checker == 'Y':
                            list_items[index_to_update][head_items.index(column_to_update)] = new_value
                            print(f"Anda telah mengubah produk {kode_produk_update}.")
                            break
                        elif checker == 'N':
                            print("Pengubahan data dibatalkan.")
                            break
                        else:
                            print("Anda memasukkan input yang salah")
                            
                else:
                    print("Nama kolom yang anda masukkan tidak tersedia.")
            else:
                print("Kode produk yang anda masukkan tidak tersedia.")
        # Input '2' untuk kembali ke menu sebelumnya
        elif menu_input_3 == "2":
            print()
            menu_3_display()
            break
        else:
            print()
            print('Mohon masukkan input menu dengan benar!')
            print()
            continue

# Fungsi seller untuk menghapus produk dari daftar produk pakan
# Terdapat pilihan input: '1' untuk menghapus pakan tertentu, '2' untuk menghapus semua produk pakan, '3' untuk kembali ke menu sebelumnya 
def menu_4():
    if list_items == []:
        print('Daftar produk kosong!')
        return
    while True:
        menu_4_display()
        display_items()
        menu_input_4 = input('Masukkan angka menu yang anda inginkan (1/2/3): ')
        # Input '1' untuk menghapus produk pakan tertentu, berdasarkan kode produk yang diberikan
        if menu_input_4 == '1':
            if list_items == []:
                print('Daftar produk kosong!')
                return
            # Memasukkan kode produk yang akan dihapus
            kode_produk_hapus = input('Masukkan kode produk yang akan dihapus: ').upper()
            # Mencari indeks produk yang akan dihapus
            index_to_delete = None
            for i, item in enumerate(list_items):
                if item[0] == kode_produk_hapus:
                    index_to_delete = i
                    break
            if index_to_delete is not None:
                checker = input("Apakah anda yakin ingin menghapus produk ini? (Y/N)").upper()
                if checker == 'Y':
                    del list_items[index_to_delete]
                    print(f"Data produk pakan dengan kode {kode_produk_hapus} telah dihapus.")
                elif checker == 'N':
                    print(f"Data produk pakan dengan kode {kode_produk_hapus} tidak dihapus.")
                else:
                    print("Anda memasukkan input yang salah")
                    continue
            else:
                print("Kode produk yang anda cari tidak tersedia.")
        # Input '2' untuk menghapus semua produk pakan dalam daftar
        elif menu_input_4 == "2":
            if list_items == []:
                print('Daftar produk kosong!')
                return
            checker = input("Apakah anda yakin ingin menghapus semua produk? (Y/N)").upper()
            if checker == 'Y':
                list_items.clear()
                print("Semua data produk telah dihapus.")
            elif checker == 'N':
                print("Data produk tidak dihapus.")
            else:
                print("Anda memasukkan input yang salah")
                continue
        # Input '3' untuk kembali ke menu sebelumnya
        elif menu_input_4 == "3":
            break
        else:
            print('Mohon masukkan input menu dengan benar!')


# Fungsi customer atau pembeli
# Pembeli bisa melihat/mencetak daftar produk pakan dan membeli pakan
# Terdapat pilihan input: input '1' untuk melihat daftar produk, '2' untuk membeli produk pakan, '3' untuk kembali ke menu sebelumnya 
def feed_customer():
    while True:
        # Input '1' untuk melihat semua produk yang tersedia di daftar produk
        display_customer_menu()
        buyer_menu_input = input("Masukkan angka menu yang ingin dijalankan: ")
        if buyer_menu_input == '1':
            if list_items == []:
                print('Daftar produk kosong!')
                return
            while True:
                menu_1_display()
                menu_input_1 = input('Masukkan angka menu yang anda inginkan (1/2/3/4/5): ')
                # Input '1' untuk menampilkan semua daftar produk pakan
                if menu_input_1 == '1':
                    display_items()
                # Input '2' untuk menampilkan produk pakan tertentu
                elif menu_input_1 == '2':
                    kode_pakan_input = input('Masukkan kode produk pakan yang diinginkan: ').upper()
                    for item in list_items:
                        if item[0] == kode_pakan_input:
                            print(tabulate([item], headers=head_items, tablefmt="fancy_grid"))
                            break
                    else:
                        print("Kode produk tidak ditemukan!")
                # Input '3' untuk menampilkan produk pakan berdasarkan harga terendah
                elif menu_input_1 == '3':
                    print("Daftar produk setelah diurutkan berdasarkan harga:")
                    sorted_produk_murah = sort_by_price_asc(list_items)
                    print(tabulate(sorted_produk_murah, headers=head_items, tablefmt="fancy_grid"))
                # Input '4' untuk menampilkan produk pakan berdasarkan harga tertinggi
                elif menu_input_1 == '4':
                    print("Daftar produk setelah diurutkan berdasarkan harga:")
                    sorted_produk_mahal = sort_by_price_desc(list_items)
                    print(tabulate(sorted_produk_mahal, headers=head_items, tablefmt="fancy_grid"))
                # Input '5' Kembali ke menu sebelumnya
                elif menu_input_1 == '5':
                    break
                else:
                    print('Mohon masukkan input menu dengan benar!')
        # Input '2' untuk membeli pakan yang tersedia di daftar produk    
        elif buyer_menu_input == '2':
            if list_items == []:
                print('Daftar produk kosong!')
                return
            display_items()
            kode_produk_beli = input("Masukkan kode produk yang ingin dibeli: ").upper()
            produk_ditemukan = False
            for item in list_items:
                if item[0] == kode_produk_beli:
                    produk_ditemukan = True
                    harga_per_sak = item[5]  # Harga per sak produk
                    stok_produk = item[4]    # Stok produk
                    break
            if not produk_ditemukan:
                print("Kode produk yang anda masukkan tidak tersedia.")
            else:
                while True:
                    try:
                        kuantitas_produk_beli = int(input("Masukkan jumlah produk pakan yang ingin dibeli (dalam sak): "))
                        if kuantitas_produk_beli < 0:
                            print("Jumlah produk yang ingin dibeli harus lebih besar dari nol.")
                            continue
                        elif kuantitas_produk_beli > stok_produk:
                            print("Stok tidak cukup untuk memenuhi pesanan.")
                            continue
                        else:
                            total_harga = harga_per_sak * kuantitas_produk_beli
                            print(f"Total harga yang harus dibayar: Rp {total_harga}")
                            # Melakukan konfirmasi pembelian
                            konfirmasi_pembelian = input(f"Apakah anda yakin untuk membeli {item[1]} kode {kode_produk_beli} sebanyak {kuantitas_produk_beli} sebesar {total_harga}? (Y/N): ").upper()
                            if konfirmasi_pembelian == 'Y':
                                uang_diberikan = int(input("Masukkan jumlah uang yang ingin dibayarkan: "))
                                if uang_diberikan < total_harga:
                                    kurang_bayar = total_harga - uang_diberikan
                                    print(f"Transaksi dibatalkan. Dana anda kurang sebesar Rp {kurang_bayar} untuk menyelesaikan transaksi.")
                                elif uang_diberikan == total_harga:
                                    print("Terima kasih telah menyelesaikan transaksi.")
                                    # Mengurangi stok produk yang dibeli dari stok yang tersedia
                                    item[4] -= kuantitas_produk_beli
                                else:
                                    lebih_bayar = uang_diberikan - total_harga
                                    print(f"Ambil uang kembalian Anda sebesar Rp {lebih_bayar}. Terima kasih telah menyelesaikan transaksi.")
                                    item[4] -= kuantitas_produk_beli
                                break
                            elif konfirmasi_pembelian == 'N':
                                print("Transaksi dibatalkan.")
                                break
                            else:
                                print("Masukkan input yang valid (Y/N).")
                    except ValueError:
                        print("Masukkan angka yang valid untuk jumlah produk yang ingin dibeli.")
                        continue
        # Input '3' untuk kembali ke menu sebelumnya
        elif buyer_menu_input == '3':
            print("Terima kasih!")
            break
        else:
            print('Mohon masukkan input menu dengan benar!')

if __name__ == "__main__":
    program()



