"""
Masala: 3 xonali natural son berilgan.
Uning o`ngdan birinchi raqamini o`chirib, chap tarafga
yozishdan hosil bo`lgan sonni aniqlovchi dastur tuzilsin;
"""

son = input("\n3 xonali natural son kiriting: ")
try:
    son = int(son)
except:
    natija = "\nNoto`g`ri qiymat kiritildi!\n"
else:
    if 99 < son < 1000:
        
        natija =f'{son} sonini {son%10}{son//100}{son//10%10} raqamlar joyini o`zgartirdik\n'
    else:
        natija = "\nNoto`g`ri qiymat kiritildi!\n"

print(natija)
