import random
import string
import time

def random_string(panjang:int) -> str:
    '''Membuat Huruf Random'''
    hasil_string = ''.join(random.choice(string.ascii_letters) for i in range(panjang))
    return hasil_string

def date_now():
    '''Mengambil Waktu Sekarang'''
    hasil_date = time.strftime('%Y-%m-%d %H.%M.%S %z', time.gmtime())
    return hasil_date