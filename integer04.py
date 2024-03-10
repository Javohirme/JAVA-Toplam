"""
Masala: a va b musbat sonlar berilgan.
a uzunlikdagi kesmada b uzunlikdagi kesmani necha marta
joylashtirish mumkinligini aniqlovchi dastur tuzilsin;
05.03.2024
"""

a = input("\nA uzunlikni kiriting: ")
b = input("B uzunlikni kiriting: ")

try:
    a = float(a)
    b = float(b)
except:
    natija = "\nNoto`g`ri qiymat kiritildi!\n"
else:
    if a > 0 and b > 0:
        natija = f"{a} uzunlikdagi kesmada {b} uzunlikdagi kesma {int(a/b)} marta joylashtirish mumkin."
    else:
        natija = "Musbat son kiritilmadi\n"

print(natija)
