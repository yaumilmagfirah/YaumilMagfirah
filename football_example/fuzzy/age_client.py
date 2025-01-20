import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Definisikan rentang umur
x_age = np.arange(0, 100, 1)

# Buat fungsi keanggotaan fuzzy untuk kategori 'muda', 'parubaya', dan 'tua'
muda = fuzz.trapmf(x_age, [0, 0, 25, 30])      # 'muda' berangsur-angsur hilang di umur 30
parubaya = fuzz.trimf(x_age, [25, 40, 55])     # 'parubaya' memiliki nilai puncak antara 30-50
tua = fuzz.trapmf(x_age, [50, 55, 100, 100])   # 'tua' mulai dari umur 50 ke atas

age = 29
muda_degree = fuzz.interp_membership(x_age, muda, age)
parubaya_degree = fuzz.interp_membership(x_age, parubaya, age)
tua_degree = fuzz.interp_membership(x_age, tua, age)

print(f"Keanggotaan usia {age} tahun:")
print(f"  Muda: {muda_degree}")
print(f"  Parubaya: {parubaya_degree}")
print(f"  Tua: {tua_degree}")
