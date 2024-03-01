from . import Database
from . import Util
import os

def read(**kwargs):
    '''Operasi Membaca File'''
    try:
        with open(Database.DB_NAME,'r') as file:
            content = file.readlines()
            jumlah_buku = len(content)
            if 'index' in kwargs:
                index_buku = kwargs['index']-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:
                    return content[index_buku]
            else:
                return content
    except:
        print('Membaca Database Error')
        return False
    
def create(judul, penulis, tahun):
    '''Operasi Memasukkan Data ke File'''
    data = Database.TEMPLATE.copy()
    data['pk'] = Util.random_string(6)
    data['date_add'] = Util.date_now()
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['tahun'] = str(tahun)
    
    data_str = f"{data['pk']},{data['date_add']},{data['judul']},{data['penulis']},{data['tahun']}\n"
    
    try:
        with open(Database.DB_NAME,'a', encoding='utf-8') as file:
            file.write(data_str)
    except Exception as e:
        print(f'Terjadi kesalahan: {e}')
        
def update(no_buku, pk, date_add, judul, penulis, tahun):
    '''Operasi Memasukkan Data Update ke File'''
    data = Database.TEMPLATE.copy()
    data['pk'] = pk
    data['date_add'] = date_add
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['tahun'] = str(tahun)
    
    data_str = f"{data['pk']},{data['date_add']},{data['judul']},{data['penulis']},{data['tahun']}\n"
    data_length = len(data_str)
    
    try:
        with open(Database.DB_NAME,'r+', encoding='utf-8') as file:
            file.seek(data_length*(no_buku-1)+(no_buku-1))
            file.write(data_str)
    except Exception as e:
        print(f'Terjadi kesalahan: {e}')
        
def delete(no_buku):
    '''Operasi Menghapus Data di File'''
    try:
        with open(Database.DB_NAME,'r') as file:
            count = 0
            while True:
                content = file.readline()
                if len(content) == 0:
                    break
                elif count == no_buku-1:
                    pass
                else:
                    with open('temp_data.txt','a') as temp_data:
                        temp_data.write(content)
                count += 1
    except Exception as e:
        print(f'Terjadi kesalahan: {e}')
        
    os.replace('temp_data.txt',Database.DB_NAME)