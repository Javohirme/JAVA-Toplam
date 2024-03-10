"""
2 xonali son berilgan. Uning raqamlari yig`indisini aniqlovchi dastur tuzilsin;
"""

son = input("\nIkki xonali son kiriting: ")

try:
    son = float(son)
except:
    natija = "\nNot`g`ri qiymat kiritildi!\n"
else:
    if son > 9 and son < 100:
        natija = (
            f"Berilgan {son} sonni raqamlar yig`ndisi {(son//10)+(son%10)} ga teng\n"
        )
    else:
        natija = "\nNot`g`ri qiymat kiritildi!\n"

print(natija)
