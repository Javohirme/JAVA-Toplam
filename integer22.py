"""
Masala: Kun boshidan boshlab n soniya vaqt o`tdi.
Kun boshidan boshlab qancha soat va soniya o`tganini aniqlovchi dastur tuzilsin;
09.03.2024
"""

n = input("\nKun boshidan boshlab qancha soniya o`tdi: ")
try:
    n = float(n)
except:
    natija = "\nNoto`g`ri qiymat kiritildi!\n"
else:
    if n > -1:
        natija = f"{n} soniyada {n//3600} soat {n%3600} soniya mavjud.\n"
    else:
        natija = "\nNoto`g`ri qiymat kiritildi!\n"

print(natija)
