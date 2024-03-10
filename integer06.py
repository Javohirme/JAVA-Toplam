"""
Masala: 2 xonali son berilgan. Oldin uning o`nlar xonasidagi raqamni,
so`ng birlar xonasidagi raqamni chiqaruvchi dastur tuzilsin;
"""

son = input("\nIkki xonali son kiriting: ")
try:
    son = float(son)
except:
    natija = "\nNoto`g`ri qiymat kiritildi\n"
else:
    if son > 9 and son < 100:
        natija = f"{son} sonida, o`nlar xonasidagi raqam {int(son//10)} ga teng va birlar xonasidagi raqam {int(son%10)}"
    else:
        natija = "\nNoto`g`ri qiymat kiritildi\n"

print(natija)
