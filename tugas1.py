#Tugas 1
# Buat program Python yang menampilkan angka 1 sampai 100.

# Aturan:
# - Angka kelipatan 3 diganti dengan "Dang".
# - Angka kelipatan 5 diganti dengan "Dut".
# - Angka kelipatan 3 sekaligus 5 diganti dengan "Dangdut".
# - Angka lainnya ditampilkan seperti biasa.

#Tanpa Function

for i in range (1,101,1) :
    #print(i)
    #print (type(i))
    if i % 3 == 0 and i % 5 == 0 :
        print ('Dangdut')
    elif i % 3 == 0 :
        print ('Dang')
    elif i % 5 == 0 :
        print ('Dut')
    else :
        print(i)

# Pakai Function

def bilangan (b) :
    if b % 3 == 0 and b % 5 == 0 :
        return 'Dangdut'
    elif b % 3 == 0 :
        return 'Dang'
    elif b % 5 == 0 :
        return 'Dut'
    else :
        return b

for i in range (1,101,1) :
    print(bilangan(i))