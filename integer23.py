"""
Masala: Kun boshidan boshlab n soniya vaqt o`tdi.
Kun boshidan boshlab qancha soat, daqida, soniya o`tganini aniqlovchi dastur tuzilsin;
"""

n = input("\nKun boshidan boshlab qancha soniya o`tdi: ")
try:
    n = float(n)
except:
    natija = "\nNoto`g`ri qiymat kiritildi!\n"
else:
    if n > -1:
        natija = f"{n} soniyada {n//3600} soat {n%3600//60} daqiqa {n%60} soniya mavjud"
    else:
        natija = "\nNoto`g`ri qiymat kiritildi!\n"

print(natija)
