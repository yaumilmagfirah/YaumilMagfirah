import numpy as np
import skfuzzy as fuzz

def output_to_crisp_value(output):
    """
    Mengubah label fuzzy menjadi nilai crisp sebagai contoh.
    
    Parameters:
    output (str): Nama dari output fuzzy, seperti "rendah", "sedang", "tinggi".
    
    Returns:
    float: Nilai crisp yang sesuai dengan label fuzzy.
    """
    # Mapping dari label fuzzy ke nilai crisp (contoh)
    crisp_mapping = {
        "rendah": 20,
        "sedang": 50,
        "tinggi": 80
    }
    
    return crisp_mapping.get(output, 0)  # Nilai default adalah 0 jika tidak ditemukan

def defuzzification(rules, method="centroid"):
    """
    Melakukan defuzzification untuk mendapatkan nilai crisp dari aturan fuzzy.
    
    Parameters:
    rules (dict): Aturan fuzzy yang berisi output dengan nilai membership degree.
    method (str): Metode defuzzification, default "centroid".
    
    Returns:
    float: Nilai crisp sebagai hasil defuzzification.
    """
    # Jika menggunakan metode centroid
    if method == "centroid":
        # Numerator dan denominator untuk perhitungan centroid
        numerator = 0.0
        denominator = 0.0
        
        # Menghitung centroid berdasarkan hasil aturan fuzzy
        for output, degree in rules.items():
            # Misalkan kita mendefinisikan nilai crisp dari output sebagai contoh
            crisp_value = output_to_crisp_value(output)
            numerator += degree * crisp_value
            denominator += degree
        
        # Menghindari pembagian dengan nol
        if denominator == 0:
            return 0
        
        # Nilai centroid
        return numerator / denominator

    else:
        raise ValueError(f"Method {method} tidak didukung.")
    
def fuzzy_input(name, **membership_degrees):
    """
    Membuat variabel fuzzy dengan beberapa derajat keanggotaan.
    
    Parameters:
    name (str): Nama dari variabel fuzzy.
    **membership_degrees (dict): Nama dan nilai dari derajat keanggotaan,
                                 misalnya rendah=0.2, sedang=0.5, tinggi=0.8
    
    Returns:
    dict: Representasi variabel fuzzy dengan nama dan derajat keanggotaan.
    """
    # Membuat dictionary untuk menyimpan derajat keanggotaan dari variabel fuzzy
    fuzzy_var = {
        "name": name,
        "memberships": membership_degrees
    }
    return fuzzy_var

# Contoh Pseudocode Fuzzy
# Definisikan variabel input sebagai derajat keanggotaan
partisipasi = fuzzy_input("Partisipasi", rendah=0.2, sedang=0.5, tinggi=0.8)
uts_uas_tugas = fuzzy_input("UTS_UAS_Tugas", buruk=0.3, cukup=0.6, baik=0.9)
commit = fuzzy_input("Commit", sedikit=0.2, sedang=0.5, banyak=0.8)
penambahan_kode = fuzzy_input("PenambahanKode", sedikit=0.2, sedang=0.5, banyak=0.9)
penghapusan_kode = fuzzy_input("PenghapusanKode", sedikit=0.3, sedang=0.6, banyak=0.85)

# Definisikan aturan fuzzy
rules = [
    ("Sangat Baik", min(partisipasi["tinggi"], uts_uas_tugas["baik"], commit["banyak"], penambahan_kode["banyak"])),
    ("Baik", min(partisipasi["sedang"], uts_uas_tugas["baik"], commit["sedang"], penambahan_kode["sedang"])),
    ("Cukup", min(partisipasi["sedang"], uts_uas_tugas["cukup"], commit["sedang"])),
    ("Kurang", min(partisipasi["rendah"], uts_uas_tugas["buruk"]))
]

# Hitung hasil dengan metode defuzzifikasi
output = defuzzification(rules, method="centroid")

# Output adalah nilai akhir “crisp”
print("Nilai Akhir:", output)
