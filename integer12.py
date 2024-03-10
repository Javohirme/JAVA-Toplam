"""
Masala: 3 xonali natural son berilgan.
Uning raqamlarini teskari tartibda yozishdan
hosil bo`lgan sonni aniqlovchi dastur tuzilsin;
08.03.2024
"""

son = input("\n3 xonali natural son kiriting: ")
try:
    son = int(son)
except:
    natija = "\nNoto`g`ri qiymat kiritildi!\n"
else:
    if 99 < son < 1000:
        natija = f"{son} sonini teskari tartibda {int(str(son)[::-1])} yozildi.\n"
    else:
        natija = "\nNoto`g`ri qiymat kiritildi!\n"

print(natija)
