"""
Masala: Kun boshidan boshlab n soniya vaqt o`tdi.
Kun boshidan boshlab qancha daqiqa va soniya o`tganini aniqlovchi dastur tuzilsin;
"""

n = input("\nKun boshidan boshlab qancha soniya o`tdi: ")
try:
    n = float(n)
except:
    natija = "\nNoto`g`ri qiymat kiritildi\n"
else:
    if n >= 0:
        natija = f"{n} soniya ichida {int(n//60)} daqiqa va {int(n%60)} soniya mavjud\n"
    else:
        natija = "\nNoto`g`ri qiymat kiritildi\n"

print(natija)
