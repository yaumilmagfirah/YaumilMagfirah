import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Fungsi untuk mengonversi nilai numerik ke huruf (A, B, C, D)
def konversi_ke_huruf(nilai):
    if nilai >= 85:
        return 'A'
    elif nilai >= 70:
        return 'B'
    elif nilai >= 60:
        return 'C'
    else:
        return 'D'
    
# Step 1: Definisikan Variabel Fuzzy
# Input: Partisipasi, Tugas, Ujian
partisipasi = ctrl.Antecedent(np.arange(0, 11, 1), 'partisipasi')
tugas = ctrl.Antecedent(np.arange(0, 11, 1), 'tugas')
ujian = ctrl.Antecedent(np.arange(0, 11, 1), 'ujian')

# Output: Nilai Akhir
nilai_akhir = ctrl.Consequent(np.arange(0, 101, 1), 'nilai_akhir')

# Step 2: Definisikan Fungsi Keanggotaan
# Partisipasi (rendah, sedang, tinggi)
partisipasi['rendah'] = fuzz.trapmf(partisipasi.universe, [0, 0, 3, 5])
partisipasi['sedang'] = fuzz.trimf(partisipasi.universe, [3, 5, 7])
partisipasi['tinggi'] = fuzz.trapmf(partisipasi.universe, [5, 7, 10, 10])

# Tugas (buruk, cukup, baik)
tugas['buruk'] = fuzz.trapmf(tugas.universe, [0, 0, 3, 5])
tugas['cukup'] = fuzz.trimf(tugas.universe, [3, 5, 7])
tugas['baik'] = fuzz.trapmf(tugas.universe, [5, 7, 10, 10])

# Ujian (buruk, cukup, baik)
ujian['buruk'] = fuzz.trapmf(ujian.universe, [0, 0, 3, 5])
ujian['cukup'] = fuzz.trimf(ujian.universe, [3, 5, 7])
ujian['baik'] = fuzz.trapmf(ujian.universe, [5, 7, 10, 10])

# Nilai Akhir (D, C, B, A)
nilai_akhir['D'] = fuzz.trapmf(nilai_akhir.universe, [0, 0, 40, 60])
nilai_akhir['C'] = fuzz.trimf(nilai_akhir.universe, [40, 60, 70])
nilai_akhir['B'] = fuzz.trimf(nilai_akhir.universe, [60, 70, 85])
nilai_akhir['A'] = fuzz.trapmf(nilai_akhir.universe, [70, 85, 100, 100])

# Step 3: Definisikan Aturan Fuzzy
rule1 = ctrl.Rule(partisipasi['rendah'] & tugas['buruk'] & ujian['buruk'], nilai_akhir['D'])
rule2 = ctrl.Rule(partisipasi['rendah'] & tugas['cukup'] & ujian['cukup'], nilai_akhir['C'])
rule3 = ctrl.Rule(partisipasi['sedang'] & tugas['cukup'] & ujian['cukup'], nilai_akhir['C'])
rule4 = ctrl.Rule(partisipasi['tinggi'] & tugas['cukup'] & ujian['cukup'], nilai_akhir['B'])
rule5 = ctrl.Rule(partisipasi['tinggi'] & tugas['baik'] & ujian['baik'], nilai_akhir['A'])

# Step 4: Buat Sistem Kontrol dan Simulasi
nilai_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
nilai_simulasi = ctrl.ControlSystemSimulation(nilai_ctrl)

# Step 5: Masukkan Nilai Input untuk Menghitung Output
nilai_simulasi.input['partisipasi'] = 3
nilai_simulasi.input['tugas'] = 4
nilai_simulasi.input['ujian'] = 4

# Visualisasi (opsional)
# partisipasi.view()
# tugas.view()
# ujian.view()
# nilai_akhir.view(sim=nilai_simulasi)

# Jalankan simulasi
nilai_simulasi.compute()

# Dapatkan output nilai akhir
hasil_nilai_akhir = nilai_simulasi.output['nilai_akhir']
# print("Nilai simulasi:", nilai_simulasi)
print("Nilai Akhir Mahasiswa:", hasil_nilai_akhir)
print("Nilai Akhir Mahasiswa:", konversi_ke_huruf(hasil_nilai_akhir))
