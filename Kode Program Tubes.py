#PEMBUATAN DICTIONARY DAN LIST KOSONG.
klub = {} #dictionary kosong yang akan diisi dengan key nama tim dan value berupa list yang elemennya adalah total gol dan jumlah bertanding dari suatu tim.
list_key1 = [] #list kosong untuk menyimpan data file teks kolom 1/nama tim 1.
list_key2 = [] #list kosong untuk menyimpan data file teks kolom 4/nama tim 2.
list_val1 = [] #list kosong untuk menyimpan data file teks kolom 2/perolehan gol tim 1.
list_val2 = [] #list kosong untuk menyimpan data file teks kolom 3/perolehan gol tim 2.

#PEMBUATAN FUNGSI PEMBACAAN FILE TEKS.
def read_file(file_name):
    file = open(file_name, "r") #open file teks.
    for i in file: #memasukan data file teks ke dalam list_key1, list_key2, list_val1, list_val2 dengan menggunakan perulangan.
        (key1, val1, val2, key2) = i.split() #data file teks displit menjadi 4 bagian yaitu key1, val1, val2, key2.
        list_key1.append(key1) #menambahkan data dari file teks kolom 1 ke dalam list_key1.
        list_val1.append(val1) #menambahkan data dari file teks kolom 2 ke dalam list_val1.
        list_val2.append(val2) #menambahkan data dari file teks kolom 3 ke dalam list_val2.
        list_key2.append(key2) #menambahkan data dari file teks kolom 4 ke dalam list_key2.
        join_list = list_key1 + list_key2 #menggabungkan list_key1 dan list_key2 dan diletakkan dalam variabel join_list dan nantinya memudahkan untuk mencari jumlah pertandingan dari sebuah tim.
    
    #mengcasting tipe data join_list dari list ke set.
    set1 = set(join_list) #casting join_list dari list menjadi set yang dimisalkan sebagai set1.
    list_set1 = list(set1) #casting set1 menjadi list yang dimisalkan sebagai list_set1.
    list_set1.sort() #mengurutkan list dengan fungsi sort.
    
    #menambahkan list_key1, list_key2, list_val1, list_val2 ke dalam dictionary klub dengan perulangan.
    for i in list_set1:
        list_value = [] #list kosong sebagai value dari dictionary klub.

        #menggunakan fungsi if yang nantinya digunakan untuk menentukan total gol dari sebuah tim.
        if i in list_key1 and i in list_key2: 
            indeks_list_key1 = list_key1.index(i) #indeks list_key1 untuk mencari gol yang dibuat oleh sebuah tim.
            indeks_list_key2 = list_key2.index(i) #indeks list_key2 untuk mencari gol yang dibuat oleh sebuah tim.
            total_gol = int(list_val1[indeks_list_key1]) + int(list_val2[indeks_list_key2]) #mencari total gol dan casting tipe data ke integer.
            jumlah_pertandingan = join_list.count(i) #mencari banyak bertanding dari sebuah tim dengan menggunakan fungsi count.
            list_value.append(total_gol) #menambahkan total gol ke dalam list_value.
            list_value.append(jumlah_pertandingan) #menambahkan jumlah bertanding ke dalam list_value.
            klub[i] = list_value #memasukan list_value ke dalam dictionary klub sebagai value dari dictionary tersebut.
        elif i in list_key1:
            indeks_list_key1 = list_key1.index(i) #indeks list_key1 untuk mencari gol yang dibuat oleh sebuah tim.
            total_gol = int(list_val1[indeks_list_key1]) #mencari total gol dan casting tipe data ke integer.
            jumlah_pertandingan = join_list.count(i) #mencari banyak bertanding dari sebuah tim dengan menggunakan fungsi count.
            list_value.append(total_gol) #menambahkan total gol ke dalam list_value.
            list_value.append(jumlah_pertandingan) #menambahkan jumlah bertanding ke dalam list_value.
            klub[i] = list_value #memasukan list_value ke dalam dictionary klub sebagai value dari dictionary tersebut.
        elif i in list_key2:
            indeks_list_key2 = list_key2.index(i) #indeks list_key2 untuk mencari gol yang dibuat oleh sebuah tim.
            total_gol = int(list_val2[indeks_list_key2]) #mencari total gol dan casting tipe data ke integer.
            jumlah_pertandingan = join_list.count(i) #mencari banyak bertanding dari sebuah tim dengan menggunakan fungsi count.
            list_value.append(total_gol) #menambahkan total gol ke dalam list_value.
            list_value.append(jumlah_pertandingan) #menambahkan jumlah bertanding ke dalam list_value.
            klub[i] = list_value #memasukan list_value ke dalam dictionary klub sebagai value dari dictionary tersebut.
    print(klub)
    file.close() #close file teks

#PEMBUATAN FUNGSI DASHBOARD.
def dashboard(dictionary_klub): #fungsi dashboard dengan dictinary sebagai parameter.
    for key, val in dictionary_klub.items(): #iterasi elemen dictionary.
        total_gol = val[0] #mengakses total gol dari value dictionary klub dengan indeks 0 untuk total gol.
        jumlah_bertanding = val[1] #mengakses jumlah bertanding dari value dictionary klub dengan indeks 1 untuk jumlah bertanding.
        rata2_gol = total_gol/jumlah_bertanding #mencari rata-rata gol dari sebuah tim.
        print(key.title().replace("_"," "),":") #mengprint nama tim lalu menggunakan title untuk mengubah setiap awal nama tim menjadi huruf kapital dan mengganti "_" menjadi spasi.
        print("Total Gol =", total_gol) #mengprint total gol dari sebuah tim. 
        print("Jumlah Bertanding =", jumlah_bertanding, "kali") #mengprint Jumlah bertanding dari sebuah tim.
        print("Rata-Rata Gol =", rata2_gol) #mengprint rata-rata gol dari sebuah tim.
        print("\n") #menggunakan Escape Sequence pindah baris untuk merapikan.

#main program.
read_file("tubes.txt")
dashboard(klub)
