from . import Operasi

def read_console():
    '''Membaca Data'''
    data_file = Operasi.read()
    
    # Header
    print('\n' + '='*100)
    print(f"{'No':^4} | {'Judul':^40} | {'Penulis':^40} | {'Tahun':^5}")
    print('-'*100)
    
    # Data
    for index, data in enumerate(data_file):
        data_break = data.split(',')
        judul = data_break[2]
        penulis = data_break[3]
        tahun = data_break[4]
        print(f'{index+1:^4} | {judul:.40} | {penulis:.40} | {tahun:4}', end='')
        
    # Footer
    print('='*100 + '\n')
    
def create_console():
    '''Membuat Data Baru'''
    print('\n' + '='*100)
    print(f"{'SILAHKAN MASUKKAN DATA BUKU':^100}")
    print('-'*100)    

    judul = input('Judul\t: ')
    penulis = input('Penulis\t: ')
    while True:
        try:
            tahun = int(input('Tahun\t: '))
            if len(str(tahun)) == 4:
                break
            else:
                print('Masukkan tahun dengan benar! (yyyy)')
        except:
            print('Masukkan tahun dengan benar! (yyyy)')
        
    Operasi.create(judul,penulis,tahun)
    print('\nBerikut adalah data baru Anda')
    read_console()
        
def update_console():
    '''Mengubah Data'''
    read_console()
    while True:
        no_buku = input('Pilih nomor buku yang akan di update: ')
        try:
            data_buku = Operasi.read(index=int(no_buku))
            if data_buku:
                break
            else:
                print('Nomor buku tidak valid!')
        except:
            print('Masukkan angka!')
    
    data_break = data_buku.split(',')
    pk = data_break[0]
    date_add = data_break[1]
    judul = data_break[2]
    penulis = data_break[3]
    tahun = data_break[4][:-1]
    
    while True:
        print('\n' + '='*100)
        print('Pilih data yang ingin Anda ubah')
        print(f'1. Judul\t: {judul:.40}')
        print(f'2. Penulis\t: {penulis:.40}')
        print(f'3. Tahun\t: {tahun:4}')
        
        user_option = input('Pilih data (1/2/3): ')
        print('-'*100)
        match user_option:
            case '1': judul = input('Judul\t: ')
            case '2': penulis = input('Penulis\t: ')
            case '3': 
                while True:
                    try:
                        tahun = int(input('Tahun\t: '))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print('Masukkan tahun dengan benar! (yyyy)')
                    except:
                        print('Masukkan tahun dengan angka! (yyyy)')
            case _: print('Pilih data yang sesuai!')
        
        print('-'*100)
        print('Data baru Anda')
        print(f'1. Judul\t: {judul:.40}')
        print(f'2. Penulis\t: {penulis:.40}')
        print(f'3. Tahun\t: {tahun:4}')
        
        is_done = input('Selesai update data? (y/n): ')
        if is_done.lower() == 'y':
            break
        
    Operasi.update(int(no_buku),pk,date_add,judul,penulis,tahun)
    
def delete_console():
    '''Menghapus Data'''
    while True:
        read_console()
        try: 
            no_buku = int(input('Pilih nomor buku yang akan di hapus: '))
            try:
                data_buku = Operasi.read(index=int(no_buku))
                if data_buku:
                    data_break = data_buku.split(',')
                    judul = data_break[2]
                    penulis = data_break[3]
                    tahun = data_break[4][:-1]
                    
                    print('\n' + '='*100)
                    print('Data yang akan Anda hapus')
                    print(f'1. Judul\t: {judul:.40}')
                    print(f'2. Penulis\t: {penulis:.40}')
                    print(f'3. Tahun\t: {tahun:4}')
                    
                    yakin = input('Apakah Anda yakin menghapus data? (y/n): ')
            
                    match yakin.lower():
                        case 'y': 
                            Operasi.delete(no_buku)
                            print('Data berhasil di hapus')
                        case 'n': pass
                        case _: print('Input yang Anda masukkan tidak sesuai')
                    
                    is_done = input('Keluar dari menu delete data? (y/n): ')
                    if is_done.lower() == 'y':
                        break
                else:
                    print('Nomor buku tidak valid!')
            except:
                print('Data tidak boleh kosong')
                break
        except:
            print('Masukkan angka!')