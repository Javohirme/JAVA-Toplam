"""
Masala: Kun boshidan boshlab n soniya vaqt o`tdi.
Kun boshidan boshlab qancha to`liq daqiqa o`tganini aniqlovchi dastur tuzilsin;
"""

n = input("\nKun boshidan boshlab nechchi soniya vaqat o`tdi: ")
try:
    n = float(n)
except:
    natija = "\nNoto`g`ri qiymat kiritildi!\n"
else:
    if n >= 0:
        natija = f"{n} soniyada to`liq {int(n//60)} daqiqa mavjud"
    else:
        natija = "\nNoto`g`ri qiymat kiritildi!\n"

print(natija)
