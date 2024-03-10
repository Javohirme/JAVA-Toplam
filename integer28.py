"""
Masala: Hafta kunlari quyidagicha tartibda berilgan:
1 - dushanba
2 - seshanba
3 - chorshanba
4 - payshanba
5 - juma
6 - shanba
7 - yakshanba
[1 ; 366] oralig`ida yotuvchi k soni berilgan.
Agar 1-yanvar haftaning n - kuniga to`g`ri kelsa (n => [1 ; 7]),
kiritilgan k - kun haftaning qaysi kuniga to`g`ri kelishini aniqlovchi dastur tuzilsin;
"""

h_k = input("\n1-yanvar haftaning nechanchi kunidan boshlandi: ")
hafta_k = [
    "yakshanba",
    "dushanba",
    "seshanba",
    "chorshanba",
    "payshanba",
    "juma",
    "shanba",
]
k = input("yilning nechanchi kuni: ")
try:
    k = int(k)
    h_k = int(h_k)
except:
    natija = "\nNoto`g`ri qiymat kiritildi!\n"
else:
    if 0 < h_k < 8 and 0 < k < 367:
        natija = f"1-yanvar haftaning {hafta_k[h_k]} kundan boshlangan bo`lsa,\nyilning {k} kuni haftaning {hafta_k[k%7]} ga to`gri keladi.\n"
    else:
        natija = "\nNoto`g`ri qiymat kiritildi!\n"

print(natija)
