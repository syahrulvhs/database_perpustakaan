from . import Operasi

DB_NAME = 'data.txt'
TEMPLATE = {
    'pk':'XXXXXX',
    'date_add':'yyyy-mm-dd h.m.s z',
    'judul':255*' ',
    'penulis':255*' ',
    'tahun':'yyyy'
}

def init_console():
    '''Mengecek Database'''
    try:
        with open(DB_NAME,'r') as file:
            print('Database tersedia, init done!')
    except:
        print('Database tidak ditemukan, silahkan membuat database baru')
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
        Operasi.create(judul, penulis, tahun)
    
        