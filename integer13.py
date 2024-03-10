"""
Masala: 3 xonali natural son berilgan.
Uning chapdan birinchi raqamini o`chirib, o`ng tarafga
yozishdan hosil bo`lgan sonni aniqlovchi dastur tuzilsin;
08.03.2024

"""

son = input("\n3 xonali son kiriting: ")
try:
    son = int(son)
except:
    natija = "\nNoto`g`ri son kiritildi!\n"
else:
    if 99 < son < 1000:
        son_100 = son//100
        son_10 = son//10%10 
        son_1 =son%10
        natija =f'{son} bu sonni  {son_10}{son_1}{son_100} ga o`zgartirdik\n'
    else:
        natija = "\nNoto`g`ri son kiritildi!\n"
print(natija)
