"""
Masala: 3 xonali natural son berilgan.
Uning birlar xonasidagi raqam bilan o`nlar xonasidagi raqamni
almashtirishdan hosil bo`lgan sonni aniqlovchi dastur tuzilsin;
"""

son = input("\n3 xonali natural son kiriting: ")
try:
    son = int(son)
except:
    natija = "\nNoto`g`ri qiymat kiritildi\n"
else:
    if 99 < son < 1000:
        natija = f"{son} sonining birlar xonasidagi raqam bilan o`nlar xonasidagi raqamni almashtirsak {son//100}{son%10}{son//10%10} ga teng bo`ladi\n"
    else:
        natija = "\nNoto`g`ri qiymat kiritildi\n"

print(natija)
