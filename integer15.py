"""
Masala: 3 xonali natural son berilgan.
Uning o`nlar xonasidagi raqam bilan yuzlar xonasidagi raqamni
almashtirishdan hosil bo`lgan sonni aniqlovchi dastur tuzilsin;
"""

son = input("\n3 xonali natural son kiriting: ")
try:
    son = int(son)
except:
    natija = "\nNoto`g`ri qiymat kiritildi\n"
else:
    if 99 < son < 1000:
        natija = f'{son} sonini raqamlarini o`zgartirsak {son//10%10}{son//100}{son%10} ga teng bo`ladi\n'
    else:
        natija = "\nNoto`g`ri qiymat kiritildi\n"
print(natija)
