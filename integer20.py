"""
Masala: Kun boshidan boshlab n soniya vaqt o`tdi.
Kun boshidan boshlab qancha to`liq soat o`tganini aniqlovchi dastur tuzilsin;
09.03.2024
"""

n = input("\nKun boshidan boshlab necha soniya o`tdi: ")
try:
    n = float(n)
except:
    natija = "\nNoto`g`ri qiymat kiritildi!\n"
else:
    if n >= 0:
        natija = f"{n} soniyada {int(n//3600)} soat mavjud.\n"
    else:
        natija = "\nNoto`g`ri qiymat kiritildi!\n"

print(natija)
