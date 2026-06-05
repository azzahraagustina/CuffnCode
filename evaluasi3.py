from multiprocessing import Pool
import time

def hitung_kuadrat(x):
    return x * x

if __name__ == '__main__':
    print("= SYSTEM CUFFNCODE: MEMULAI KOMPUTASI PARALEL =")
    start = time.time()
    
    # Menghitung angka 1 sampai 10 juta secara paralel memanfaatkan Core CPU
    with Pool() as p:
        hasil = p.map(hitung_kuadrat, range(10000000))
        
    end = time.time()
    print(f"Komputasi Selesai!")
    print(f"Total Waktu Eksekusi Paralel: {end - start:.2f} detik.")
