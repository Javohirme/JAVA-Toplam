"""
Masala: a va b musbat sonlar berilgan.
a uzunlikdagi kesmada b uzunlikdagi kesmani necha marta
joylashtirish mumkinligini va oxirgi kesmaning joylashmay
qoladigan qismini ham aniqlovchi dastur tuzilsin;
"""

a = input("\nA uzunlikdagi musbat son kiriting: ")
b = input("\nB uzunlikdagi musbat son kiriting: ")

try:
    a = float(a)
    b = float(b)
except:
    natija = "\nNoto`g`ri qiymat kiritildi.\n"
else:
    if a > 0 and b > 0:
        natija = f"{a} uzunlikdagi kesmada {b} uzunlikdagi kesma {int(a/b)} marta joylashtirish mumkin. {a%b} qoldiq qoladi.\n"
    else:
        natija = "\nNoto`g`ri qiymat kiritildi.\n"

print(natija)
