# 🎮 Game Batu Gunting Kertas Dengan AI Yang Belajar

## 📝 Deskripsi
Game Batu Gunting Kertas (Rock Paper Scissors) dengan AI yang **cerdas dan bisa belajar**! AI akan menganalisis pola pilihan Anda, memprediksi gerakan berikutnya, dan mencoba mengalahkan Anda. Semakin lama bermain, semakin pintar AI-nya!

## ✨ Fitur Utama

### 🤖 AI Yang Belajar
- **Pembelajaran Pola**: AI mencatat setiap gerakan Anda
- **Prediksi Gerakan**: AI memprediksi apa yang akan Anda pilih selanjutnya
- **Strategi Counter**: AI memilih gerakan yang mengalahkan prediksi tersebut
- **Adaptif**: Semakin banyak Anda bermain, semakin cerdas AI

### 🎯 Gameplay
- **Scoring System**: Lacak siapa yang menang
- **Statistik Real-time**: Lihat win rate AI dan pola permainan
- **Statistik Lengkap**: Analisis akhir game dengan detail pembelajaran AI
- **UI Interaktif**: Tampilan yang jelas dan mudah digunakan

## 🎮 Cara Bermain

### Instalasi & Menjalankan
```bash
# Tidak perlu instalasi apapun, Python sudah cukup
python main.py
```
atau langsung:
```bash
python game.py
```

### Kontrol Game
1. Pilih gerakan: **1 (Batu), 2 (Gunting), atau 3 (Kertas)**
2. Lihat hasil pertandingan
3. AI akan belajar dari pilihan Anda
4. Ulangi sampai Anda ingin berhenti (pilih **0**)
5. Lihat statistik akhir dan analisis pembelajaran AI

## 📊 Aturan Permainan
```
Batu ✊  ——→ Mengalahkan Gunting ✌️
Gunting ✌️ ——→ Mengalahkan Kertas ✋
Kertas ✋  ——→ Mengalahkan Batu ✊
```

## 🧠 Bagaimana AI Belajar?

### Mekanisme Pembelajaran
1. **Pencatatan Pola** - AI mencatat riwayat semua gerakan Anda
2. **Prediksi Markov** - Setelah Anda melakukan gerakan X, AI melihat gerakan apa yang sering Anda lakukan berikutnya
3. **Counter Strategy** - AI memilih gerakan yang mengalahkan prediksi tersebut
4. **Adaptasi Dinamis** - Semakin lama bermain, semakin akurat prediksinya

### Contoh Pembelajaran
```
Anda bermain: Batu → Kertas → Batu → Kertas → Batu
AI belajar:   "Setelah Batu, pemain sering main Kertas"
AI counter:   "Jadi saya akan main Gunting untuk mengalahkan!"
```

## 💡 Penjelasan Kode

### Struktur Class

#### `RockPaperScissorsAI`
- **Menyimpan:** Riwayat permainan, statistik, prediksi pola
- **Method Utama:**
  - `learn_from_player()` - Belajar dari gerakan pemain
  - `predict_next_move()` - Prediksi gerakan pemain selanjutnya
  - `choose_move()` - Pilih gerakan dengan strategi pembelajaran
  - `record_result()` - Catat hasil putaran

#### `RockPaperScissorsGame`
- **Mengelola:** Alur game, skor, tampilan
- **Method Utama:**
  - `get_player_input()` - Input dari pemain
  - `display_round()` - Tampilkan hasil putaran
  - `play()` - Main game loop

### Logika Pembelajaran
```python
# Mencatat pola
move_predictions['batu']['kertas'] += 1
# Artinya: Setelah pemain main batu, kertas digunakan 1 kali

# Prediksi
most_likely = max(predictions.items())
# Gerakan apa yang paling sering setelah gerakan terakhir?

# Counter
winning_move = get_winning_move(predicted_move)
# Pilih gerakan yang mengalahkan prediksi
```

## 🎯 Tips Bermain
- 🎲 **Variasi Gerakan**: Jangan terpola, ubah strategi Anda
- 🧠 **Pikirkan AI**: Ingat AI sedang mempelajari Anda
- 📊 **Amati Statistik**: Lihat win rate AI meningkat seiring waktu
- 🎮 **Tantang Diri Anda**: Bisakah Anda mengalahkan AI?

## 📈 Contoh Output Game

```
🎮 SELAMAT DATANG DI GAME BATU GUNTING KERTAS! 🎮
============================================================
🤖 Anda bermain melawan AI yang BISA BELAJAR!

🎯 PUTARAN 1
============================================================
🧑 Pemain  : ✊ BATU
🤖 AI     : ✌️ GUNTING

🎉 HASIL: PEMAIN MENANG! 🎉

📈 SKOR: Pemain 1 - 0 AI | Seri: 0
```

## ⚙️ Konfigurasi

Untuk menyesuaikan kesulitan AI, edit di `game.py`:
```python
self.learning_rate = 0.7  # 0.0-1.0
# 0.7 = AI menggunakan strategi learned 70% dari waktu
# 1.0 = AI selalu menggunakan strategi learned (lebih sulit)
# 0.5 = AI lebih sering random (lebih mudah)
```

## 📋 Persyaratan
- **Python 3.6+**
- **Tanpa library eksternal!** Hanya menggunakan built-in Python

## 🚀 Fitur Tambahan
- ✅ Emoji untuk tampilan yang lebih menarik
- ✅ Statistik real-time AI
- ✅ Tracking pola pemain
- ✅ Learning rate adaptif
- ✅ Analisis akhir game yang detail

## 🎓 Konsep Programming Yang Digunakan
- Object-Oriented Programming (OOP)
- Dictionary untuk penyimpanan data
- Algoritma prediksi sederhana
- State machine untuk game logic
- Pattern recognition

Selamat bermain dan menantang kecerdasan AI! 🤖🎮
