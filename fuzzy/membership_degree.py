import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Definisikan rentang umur
x_age = np.arange(0, 100, 1)

# Buat fungsi keanggotaan fuzzy untuk kategori 'muda', 'parubaya', dan 'tua'
muda = fuzz.trapmf(x_age, [0, 0, 25, 30])      # 'muda' berangsur-angsur hilang di umur 30
parubaya = fuzz.trimf(x_age, [25, 40, 55])     # 'parubaya' memiliki nilai puncak antara 30-50
tua = fuzz.trapmf(x_age, [50, 55, 100, 100])   # 'tua' mulai dari umur 50 ke atas

# Plot fungsi keanggotaan untuk visualisasi
plt.figure(figsize=(8, 4))
plt.plot(x_age, muda, 'b', linewidth=1.5, label='Muda')
plt.plot(x_age, parubaya, 'g', linewidth=1.5, label='Parubaya')
plt.plot(x_age, tua, 'r', linewidth=1.5, label='Tua')
plt.title('Fungsi Keanggotaan Fuzzy untuk Kategori Umur')
plt.xlabel('Usia (tahun)')
plt.ylabel('Derajat Keanggotaan')
plt.legend()
plt.grid(True)
plt.show()
