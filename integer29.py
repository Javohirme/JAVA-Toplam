"""
Masala: a, b, c musbat sonlar berilgan. Tomonlari a va b bo`lgan to`g`ri to`rtburchakka
tomoni c ga teng bo`lgan kvadrat eng ko`p joylashtirilsin. To`g`ri to`rtburchakka eng ko`p
joylashgan kvadratlar soni va joylashmay qolgan qismi yuzasini aniqlovchi dastur tuzilsin;
09.03.2024
"""

a = input("\nTo`g`ri to`rtburchakning a tomonini kiriting: ")
b = input("To`g`ri to`rtburchakning b tomonini kiriting: ")
c = input("Kvadrat tomonini kiriting: ")
try:
    a = float(a)
    b = float(b)
    c = float(c)
except:
    natija = "\nNoto`g`ri qiymat kiritldi!\n"
else:
    if a > 0 and b > 0 and c > 0:
        s = a * b
        s_k = c**2
        natija = f"Tomonlari {a} va {b} bo`lgan to`g`ri to`rtburchakka tomoni {c} ga teng bo`lgan kvadrat eng ko`p joylashgan kvadratlar {int(s//s_k)} va joylashmay qolgan qismi yuzasi {int(s%s_k)} ga teng"
    else:
      natija = "\nNoto`g`ri qiymat kiritldi!\n"

print(natija)        