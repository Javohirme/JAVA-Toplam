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
Agar 1-yanvar yakshanba bo`lsa, kiritilgan k - kun haftaning qaysi
kuniga to`g`ri kelishini aniqlovchi dastur tuzilsin;
09.03.2024
"""

k = input("\nYilning nechanchi kuni: ")
try:
    k = int(k)
except:
    natija = "\nNoto`g`ri qiymat kiritildi\n"
else:
    if 0 < k < 367:
        hafta_k = [
            "shanba",
            "yakshanba",
            "dushanba",
            "seshanba",
            "chorshanba",
            "payshanba",
            "juma",
            "shanba",
            "yakshanba",
        ]

        natija = f"Yilning birinchi kuni yakshanba bilan boshlanadigan yilning {k} kuni\nhaftaning {hafta_k[k%7]} kuniga to`g`ri keladi\n"
    else:
        natija = "\nNoto`g`ri qiymat kiritildi\n"

print(natija)
