"""
Masala: 999 dan katta bo`lgan natural son berilgan.
Bir marta bo`lib butun qismini va bo`lib qoldiq qismini olish operatorlaridan
foydalanib berilgan sonning yuzlar xonasidagi raqamni aniqlovchi dastur tuzilsin;
"""

son = input("\n999 dan katta bo`lgan natural son kiriting: ")
try:
    son = int(son)
except:
    natija = "\nNoto`g`ri qiymat kiritildi\n"
else:
    if son > 999:
        natija =f'{son} sonning yuzlar xonasidagi raqam {son//100%10}'
    else:
        natija = "\nNoto`g`ri qiymat kiritildi\n"

print(natija)
