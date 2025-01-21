berikan aku contoh fuzzy code untuk pemisahan kategori muda, parubaya dan tua.

muda = x < 30 tahun
parubaya = 30 tahun < x < 50 tahun
tua= x > 50 tahun

masa usia 30 tahun kurang 1 hari dikatakan masih muda? bagaimana fuzzy bisa mengatasi ini?

# jawaban
Logika fuzzy bisa mengatasi masalah kategori umur yang kaku dengan menggunakan derajat keanggotaan (membership degree). Dalam logika fuzzy, usia tidak ditentukan sebagai "muda", "parubaya", atau "tua" secara mutlak, tetapi bisa memiliki derajat keanggotaan di lebih dari satu kategori pada waktu yang bersamaan. Misalnya, seseorang yang berusia 29 tahun masih bisa dikatakan "muda" dengan keanggotaan tinggi, tetapi mungkin memiliki sedikit keanggotaan di "parubaya" juga.

# = Penjelasan Kode
## 1. Membership Functions (Fungsi Keanggotaan):

Muda: Diatur menggunakan fungsi trapezoidal (trapmf), yang dimulai dari usia 0 dan memiliki keanggotaan penuh hingga sekitar 25-30 tahun, lalu mulai berkurang.
Parubaya: Diatur menggunakan fungsi segitiga (trimf), yang mencapai puncak antara usia 30 dan 50 tahun.
Tua: Diatur menggunakan fungsi trapezoidal, dengan keanggotaan penuh mulai dari usia 55 ke atas.

## 2. Derajat Keanggotaan:

Seseorang yang berada di ambang kategori, misalnya 29 tahun (muda) atau 30 tahun (muda dan parubaya), akan memiliki sebagian keanggotaan di dua kategori. Ini mengatasi masalah ketidaktepatan yang terjadi jika menggunakan batasan kaku.

Pada usia 29 tahun, derajat keanggotaan untuk kategori "muda" akan tinggi (mungkin mendekati 1), sementara derajat untuk "parubaya" mungkin rendah (misalnya, 0.1 atau lebih kecil). Derajat keanggotaan ini memungkinkan kita menyatakan usia 29 tahun sebagai masih "muda" dengan sedikit kecenderungan ke "parubaya."

# Bagaimana Fuzzy Mengatasi Ambiguitas
Dengan pendekatan fuzzy, kategori usia tidak perlu memiliki batasan yang kaku. Usia seseorang bisa memiliki derajat keanggotaan di beberapa kategori pada saat bersamaan. Ini memungkinkan sistem untuk "melonggarkan" batasan yang sangat kaku, seperti pada contoh “usia 30 tahun kurang 1 hari”, di mana nilai keanggotaan orang tersebut akan secara bertahap berubah dari "muda" ke "parubaya" tanpa peralihan yang drastis.