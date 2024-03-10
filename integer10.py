"""
Masala: 3 xonali natural son berilgan.
Uning birlar xonasidagi va o`nlar xonasidagi raqamni aniqlovchi dastur tuzilsin;
"""

son = input("\nUch xonali son kirting: ")
try:
    son = float(son)
except:
    natija = "\nNoto`g`ri qiymat kiritildi\n"
else:
    if son > 99 and son < 1000:
        natija = f"{son} soninig birlar xonasi {son%10} ga teng, o`nlar xonasi {son%100//10} ga teng.\n"
    else:
        natija = "\nNoto`g`ri qiymat kiritildi\n"

print(natija)
