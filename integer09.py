"""
Masala: 3 xonali son berilgan.
Uning yuzlar xonasidagi raqamni aniqlovchi dastur tuzilsin.
"""

son = input("\nUch xonali son kiriting: ")
try:
    son = float(son)
except:
    natija = "\nNoto`g`ri qiymat kiritildi!\n"
else:
    if son > 99 and son < 1000:
        natija = f"{son} sonida yuzlar xonasida turgan raqam {int(son//100)} ga teng.\n"
    else:
        natija = "\nNoto`g`ri qiymat kiritildi!\n"

print(natija)
