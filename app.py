import streamlit as st


st.set_page_config(
    page_title="Belajar Python Dasar",
    page_icon="🐍",
    layout="centered",
)

st.title("🐍 Selamat Datang di Kelas Python Dasar!")
st.subheader("Mulai perjalananmu belajar pemrograman, satu langkah pada satu waktu.")

st.write(
    """
    Di sini kamu akan mengenal dasar-dasar Python dengan contoh sederhana
    dan latihan kecil. Tidak perlu pengalaman pemrograman sebelumnya—cukup
    rasa ingin tahu dan kemauan untuk mencoba.
    """
)

nama = st.text_input("Siapa namamu?", placeholder="Tulis nama di sini")
if nama.strip():
    st.success(f"Halo, {nama.strip()}! Selamat belajar Python. 🎉")

st.divider()
st.header("Apa yang akan dipelajari?")

topik = {
    "Variabel": {
        "deskripsi": "Variabel digunakan untuk menyimpan nilai agar dapat dipakai kembali.",
        "contoh": 'nama = "Budi"\numur = 16\nprint(nama, umur)',
    },
    "Tipe data": {
        "deskripsi": "Python memiliki tipe data seperti teks (str), bilangan bulat (int), dan desimal (float).",
        "contoh": 'pesan = "Halo!"  # str\njumlah = 3       # int\nharga = 2.5      # float',
    },
    "Percabangan": {
        "deskripsi": "Percabangan if dan else membantu program memilih tindakan berdasarkan kondisi.",
        "contoh": 'nilai = 80\nif nilai >= 75:\n    print("Lulus")\nelse:\n    print("Coba lagi")',
    },
    "Perulangan": {
        "deskripsi": "Perulangan menjalankan instruksi berulang kali, misalnya untuk setiap item dalam daftar.",
        "contoh": 'for angka in range(1, 4):\n    print(angka)',
    },
    "Fungsi": {
        "deskripsi": "Fungsi mengelompokkan instruksi agar mudah digunakan kembali.",
        "contoh": 'def sapa(nama):\n    print(f"Halo, {nama}!")\n\nsapa("Budi")',
    },
}

pilihan = st.selectbox("Pilih topik untuk melihat contoh:", list(topik))
st.markdown(f"### {pilihan}")
st.write(topik[pilihan]["deskripsi"])
st.code(topik[pilihan]["contoh"], language="python")

st.info("Tips: ubah contoh kodenya, jalankan, lalu amati apa yang berbeda.")
st.caption("Selamat belajar dan jangan takut mencoba hal baru! 🚀")