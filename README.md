# SauceDemo Test

## 📌 Deskripsi

SauceDemo-Test adalah proyek otomatisasi pengujian berbasis **Selenium WebDriver** dan **Python unittest framework** untuk menguji fitur login, menambahkan produk ke keranjang, dan checkout pada situs [SauceDemo](https://www.saucedemo.com/).

## 📂 Struktur Folder

```
SauceDemo-Test/
│── config/                 # Konfigurasi global proyek
│   ├── __init__.py         # Inisialisasi package
│   ├── config.py           # Variabel konfigurasi (BASE_URL, credentials, dll.)
│
│── library/                # Library umum yang digunakan dalam proyek
│   ├── __init__.py         # Inisialisasi package
│   ├── base.py             # Base class untuk setup dan teardown WebDriver
│
│── pages/                  # Page Object Model (POM) untuk setiap halaman web
│   ├── __init__.py         # Inisialisasi package
│   ├── login_page.py       # Login page object
│   ├── inventory_page.py   # Inventory page object
│   ├── cart_page.py        # Cart page object
│
│── assertions/             # Assertion helper untuk validasi test case
│   ├── __init__.py         # Inisialisasi package
│   ├── assertions.py       # Assertion methods
│
│── tests/                  # Folder yang berisi test case
│   ├── __init__.py         # Inisialisasi package
│   ├── test_saucedemo.py   # Test case utama
│
│── venv/                   # Virtual environment (opsional)
│── requirements.txt        # Daftar dependency Python
│── README.md               # Dokumentasi proyek
```

## 🔧 Instalasi dan Setup

### 1️⃣ **Clone Repository**

```sh
git clone https://github.com/maarsyaf/SauceDemo-Test.git
cd SauceDemo-Test
```

### 2️⃣ **Buat Virtual Environment (Opsional)**

```sh
python -m venv venv
source venv/bin/activate    # Untuk macOS/Linux
venv\Scripts\activate       # Untuk Windows
```

### 3️⃣ **Install Dependencies**

```sh
pip install -r requirements.txt
```

### 4️⃣ **Jalankan Test**

Jalankan semua test dengan perintah:

```sh
python -m unittest discover tests/ -v
```

Atau jalankan test spesifik:

```sh
python -m unittest tests/test_saucedemo.py -v
```

## 📌 Fitur yang Diuji

✅ **Login**

- Login dengan kredensial valid
- Login dengan kredensial tidak valid

✅ **Keranjang Belanja & Checkout**

- Menambahkan produk ke keranjang
- Melanjutkan proses checkout
- Verifikasi sukses checkout

## ⚙️ Teknologi yang Digunakan

- **Python 3.x**
- **Selenium WebDriver**
- **unittest Framework**
