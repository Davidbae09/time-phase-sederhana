import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Input Tahun dan Teks")
        
        # Mengatur ukuran jendela
        self.root.geometry("400x300")
        
        self.years = []
        self.texts = []

        # Label dan entry untuk tahun
        self.year_label = tk.Label(root, text="Masukkan Tahun:")
        self.year_label.pack(pady=10)  # Menambahkan padding vertikal
        self.year_entry = tk.Entry(root, width=30)
        self.year_entry.pack(pady=10)

        # Label dan entry untuk teks
        self.text_label = tk.Label(root, text="Masukkan Teks:")
        self.text_label.pack(pady=10)
        self.text_entry = tk.Entry(root, width=30)
        self.text_entry.pack(pady=10)

        # Tombol untuk menambah data
        self.add_button = tk.Button(root, text="Tambah Data", command=self.add_data, width=15)
        self.add_button.pack(pady=10)

        # Tombol untuk menampilkan grafik
        self.plot_button = tk.Button(root, text="Tampilkan Grafik", command=self.plot_graph, width=15)
        self.plot_button.pack(pady=10)

    def add_data(self):
        try:
            year = int(self.year_entry.get())
            text = self.text_entry.get()

            if not text:
                messagebox.showwarning("Input Error", "Teks tidak boleh kosong!")
                return

            self.years.append(year)
            self.texts.append(text)

            # Mengosongkan entry setelah menambah data
            self.year_entry.delete(0, tk.END)
            self.text_entry.delete(0, tk.END)

            messagebox.showinfo("Data Ditambahkan", f"Tahun {year} dan teks '{text}' telah ditambahkan.")
        except ValueError:
            messagebox.showerror("Input Error", "Masukkan tahun yang valid!")

    def plot_graph(self):
        if not self.years:
            messagebox.showwarning("Data Kosong", "Silakan tambahkan data sebelum menampilkan grafik.")
            return

        # Membuat fase waktu yang auto increment
        phases = list(range(1, len(self.years) + 1))

        # Membuat grafik garis
        plt.figure(figsize=(10, 6))
        plt.plot(self.years, phases, marker='o')

        # Menambahkan label dan judul
        plt.xlabel('Tahun')
        plt.ylabel('Fase Waktu')
        plt.title('Grafik Garis Fase Waktu Berdasarkan Tahun')

        # Menambahkan teks pada setiap titik
        for i in range(len(self.years)):
            plt.text(self.years[i], phases[i], self.texts[i], fontsize=9, ha='right')

        plt.xticks(self.years)  # Menampilkan tahun pada sumbu x
        plt.yticks(phases)  # Menampilkan fase waktu pada sumbu y
        plt.grid(False)  # Menghilangkan grid

        # Menampilkan grafik
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()
