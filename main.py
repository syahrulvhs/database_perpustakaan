import os
import CRUD 

if __name__ == '__main__':
    sistem_operasi = os.name
    
    match sistem_operasi:
            case 'posix': os.system('clear')
            case 'nt': os.system('cls')
            
    print(f"{'SELAMAT DATANG DI PROGRAM':^25}")
    print(f"{'DATABASE PERPUSTAKAAN':^25}")
    print(25*'=')
        
    # check database
    CRUD.init_console()
    
    while True:
        match sistem_operasi:
            case 'posix': os.system('clear')
            case 'nt': os.system('cls')
            
        print(f"{'SELAMAT DATANG DI PROGRAM':^100}")
        print(f"{'DATABASE PERPUSTAKAAN':^100}")
        print(100*'=')
        
        print(f"{'Pilih opsi 1 sampai 4':^95}")
        print(f"{'1. Read   Data':>48}")
        print(f"{'2. Create Data':>48}")
        print(f"{'3. Update Data':>48}")
        print(f"{'4. Delete Data':>48}\n")
        user_option = input('Masukkan opsi: ')
        
        match user_option:
            case '1': CRUD.read_console()
            case '2': CRUD.create_console()
            case '3': CRUD.update_console()
            case '4': CRUD.delete_console()
            case _: print('Pilih opsi yang sesuai (1/2/3/4)')
        
        is_done = input('Akhiri Program? (y/n): ')
        if is_done.lower() == 'y':
            break
        
print('PROGRAM SELESAI')