"""
Masala: 999 dan katta bo`lgan natural son berilgan.
Bir marta bo`lib butun qismini va bo`lib qoldiq qismini olish operatorlaridan
foydalanib berilgan sonning minglar xonasidagi raqamni aniqlovchi dastur tuzilsin;
08.03.2024
"""

son = input("\n999 dan katta bo`lgan natural son kiriting: ")
try:
    son = int(son)
except:
    natija = "\nNoto`g`ri qiymat kiritildi\n"
else:
    if 999 < son:
        natija = f"{son} sonining minglar xonasida {son//1000%10} raqam mavjud\n"
    else:
        natija = "\nNoto`g`ri qiymat kiritildi\n"

print(natija)
