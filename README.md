# 🛍️ Shopee Scraper

<div align="center">

![Shopee Scraper](https://img.shields.io/badge/React-19.2-61DAFB?logo=react)
![Vite](https://img.shields.io/badge/Vite-8.0-646CFF?logo=vite)
![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-4.2-06B6D4?logo=tailwindcss)
![Vercel](https://img.shields.io/badge/Deployed-Vercel-000000?logo=vercel)

**Cari produk termurah di Shopee dengan mudah dan cepat** 🚀

[🌐 Kunjungi Aplikasi](https://shopee-scraper-one.vercel.app/) • [📝 Dokumentasi](#fitur) • [🚀 Mulai](#cara-menggunakan)

</div>

---

## 📌 Tentang Proyek

**Shopee Scraper** adalah aplikasi web yang membantu Anda menemukan produk termurah di Shopee hanya dengan memasukkan kata kunci. Aplikasi ini secara otomatis mencari dan menampilkan 3 produk dengan harga terendah untuk setiap pencarian.

### ✨ Fitur Utama

- 🔍 **Pencarian Realtime** - Cari produk dengan kata kunci apapun
- 💰 **Harga Termurah** - Tampilkan 3 produk dengan harga terendah
- ⚡ **Loading yang Cepat** - Interface yang responsif dan user-friendly
- 🎨 **Design Modern** - Interface yang menarik dengan Tailwind CSS
- 📱 **Mobile Friendly** - Responsif di semua ukuran layar
- 🔗 **Direct Link** - Link langsung ke produk di Shopee

---

## 🔧 Tech Stack

| Teknologi | Versi | Deskripsi |
|-----------|-------|-----------|
| **React** | 19.2 | Frontend library |
| **Vite** | 8.0 | Build tool & dev server |
| **Tailwind CSS** | 4.2 | Utility-first CSS framework |
| **Vercel** | - | Deployment platform |

---

## 🚀 Demo

Coba aplikasi secara langsung di sini:

👉 **[https://shopee-scraper-one.vercel.app/](https://shopee-scraper-one.vercel.app/)**

Contoh pencarian:
- Compressor
- Sepatu
- Laptop
- iPhone

---

## 📥 Instalasi & Setup Lokal

### Prerequisites
- Node.js 16+ 
- npm atau yarn

### Langkah-langkah

1. **Clone repository**
```bash
git clone https://github.com/yourusername/shopee-scraper.git
cd shopee-scraper
```

2. **Install dependencies**
```bash
npm install
```

3. **Jalankan development server**
```bash
npm run dev
```

4. **Buka di browser**
```
http://localhost:5173
```

---

## 🏗️ Struktur Proyek

```
shopee-scraper/
├── src/
│   ├── App.jsx           # Komponen utama aplikasi
│   ├── main.jsx          # Entry point
│   └── index.css         # Styling
├── package.json          # Project configuration
├── vite.config.js        # Vite configuration
└── README.md             # Dokumentasi
```

---

## 📦 Available Scripts

### Development
```bash
npm run dev      # Jalankan dev server dengan hot reload
npm run build    # Build untuk production
npm run preview  # Preview production build secara lokal
npm run lint     # Jalankan ESLint
```

---

## 🔄 Cara Kerja

1. **Input Kata Kunci** - User memasukkan kata kunci produk
2. **API Request** - Aplikasi mengirim request ke backend scraper
3. **Scraping** - Backend mengakses Shopee dan mengumpulkan data produk
4. **Filter Harga** - Data diurutkan dan 3 produk termurah diambil
5. **Display** - Hasil ditampilkan dengan informasi lengkap (nama, harga, rating, link)

---

## 🌐 Backend

Aplikasi ini terhubung dengan backend Replit yang melakukan web scraping:

```
API Endpoint: https://shopee-scraperp-backend--yusufbahrudin97.replit.app/api/search
Method: GET
Parameter: keyword (string)
```

---

## 📝 Deployment

Aplikasi sudah di-deploy ke **Vercel** dan siap digunakan:

🔗 **Production URL**: https://shopee-scraper-one.vercel.app/

### Konfigurasi Vercel
- Framework: Vite + React
- Build Command: `npm run build`
- Output Directory: `dist`

---

## 🤝 Kontribusi

Kontribusi sangat diterima! Silakan buat pull request atau buka issue untuk saran dan perbaikan.

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah MIT License - lihat file LICENSE untuk detail.

---

## 👨‍💻 Author

Dibuat dengan ❤️ oleh [Yusuf Bahrudin](https://github.com/yusufbahrudin)

---

<div align="center">

**Jangan lupa untuk ⭐ star repository ini jika bermanfaat!**

</div>
