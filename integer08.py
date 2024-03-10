"""
Masala: 2 xonali son berilgan. Uning raqamlari o`rnini
almashtirishdan hosil bo`lgan sonni aniqlovchi dastur tuzilsin;
"""

son = input("\nIkki xonali son kiriting: ")
try:
    son = float(son)
except:
    natija = "\nNoto`g`ri qiymat kiritildi!\n"
else:
    if son > 9 and son < 100:
        son = int(son)
        son_t = int(str(son)[::-1])
        natija = f"Berilgan {son} sonning raqamlar o`rnini almashtirishdan hosil bo`lgan son {son_t} ga teng"
    else:
        natija = "\nNoto`g`ri qiymat kiritildi!\n"

print(natija)
