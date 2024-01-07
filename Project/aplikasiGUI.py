from tkinter import *
from tkinter import ttk
from ttkbootstrap import Style

def hitung_zakat_fitrah():
    try:
        jumlah_jiwa = int(entry_jiwa.get())
        harga_beras = int(entry_beras.get())
        zakat_fitrah = jumlah_jiwa * 2.5 * harga_beras
        label_hasil["text"] = f"Zakat fitrah yang harus dibayar adalah Rp. {zakat_fitrah}"
    except ValueError:
        label_hasil["text"] = "Masukkan jumlah jiwa dan harga beras dengan benar."

def hitung_zakat_maal():
    try:
        harta = int(entry_harta.get())
        nisab_emas = 85  # Nisab dalam gram emas per tahun
        nisab_harga_emas = 1080000  # Harga 1 gram emas dalam Rupiah
        
        # Konversi harta ke gram emas
        harta_gram_emas = harta / nisab_harga_emas  

        if harta_gram_emas >= nisab_emas:
            zakat_maal = harta * 0.025
            label_hasil["text"] = f"Zakat maal yang harus dibayar adalah Rp. {zakat_maal}"
        else:
            label_hasil["text"] = f"Tidak wajib membayar zakat maal karena harta belum mencapai nisab (Nisab 85gram emas/tahun atau Rp.91.800.000)."
    except ValueError:
        label_hasil["text"] = "Masukkan jumlah harta dengan benar."

style = Style(theme='vapor')

window = style.master
window.title("Aplikasi GUI Menghitung Zakat")
window.geometry("900x500")

label_judul = ttk.Label(window, text="Aplikasi Menghitung Zakat", font=("Arial", 16))
label_judul.pack(pady=10)

notebook = ttk.Notebook(window)
notebook.pack(pady=10)

frame_fitrah = ttk.Frame(notebook)
frame_fitrah.pack()

label_jiwa = ttk.Label(frame_fitrah, text="Jumlah Orang dalam Keluarga:")
label_jiwa.pack(pady=5)
entry_jiwa = ttk.Entry(frame_fitrah)
entry_jiwa.pack(pady=5)

label_beras = ttk.Label(frame_fitrah, text="Harga Beras per Kg:")
label_beras.pack(pady=5)
entry_beras = ttk.Entry(frame_fitrah)
entry_beras.pack(pady=5)

button_fitrah = ttk.Button(frame_fitrah, text="Hitung Zakat Fitrah", command=hitung_zakat_fitrah)
button_fitrah.pack(pady=10)

notebook.add(frame_fitrah, text="Zakat Fitrah")

frame_maal = ttk.Frame(notebook)
frame_maal.pack()

label_harta = ttk.Label(frame_maal, text="Jumlah Harta:")
label_harta.pack(pady=5)
entry_harta = ttk.Entry(frame_maal)
entry_harta.pack(pady=5)

button_maal = ttk.Button(frame_maal, text="Hitung Zakat Maal", command=hitung_zakat_maal)
button_maal.pack(pady=10)

notebook.add(frame_maal, text="Zakat Maal")

label_hasil = ttk.Label(window, text="Hasil perhitungan akan muncul di bawah sini", font=("Arial", 12))
label_hasil.pack(pady=10)

window.mainloop()