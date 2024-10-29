import matplotlib.pyplot as plt

def main():
    # List untuk menyimpan tahun dan teks
    years = []
    texts = []

    while True:
        # Menginput tahun
        year = input("Masukkan tahun (atau ketik 'selesai' untuk mengakhiri): ")
        if year.lower() == 'selesai':
            break
        
        # Menginput teks
        text = input("Masukkan teks untuk tahun {}: ".format(year))
        
        # Menambahkan tahun dan teks ke dalam list
        years.append(int(year))
        texts.append(text)

    # Membuat fase waktu yang auto increment
    phases = list(range(1, len(years) + 1))

    # Membuat grafik garis
    plt.figure(figsize=(10, 6))
    plt.plot(years, phases, marker='o')

    # Menambahkan label dan judul
    plt.xlabel('Tahun')
    plt.ylabel('Fase Waktu')
    plt.title('Grafik Garis Fase Waktu Berdasarkan Tahun')

    # Menambahkan teks pada setiap titik
    for i in range(len(years)):
        plt.text(years[i], phases[i], texts[i], fontsize=9, ha='right')

    plt.xticks(years)  # Menampilkan tahun pada sumbu x
    plt.yticks(phases)  # Menampilkan fase waktu pada sumbu y
    plt.grid(False)  # Menghilangkan grid

    # Menampilkan grafik
    plt.show()

if __name__ == "__main__":
    main()
