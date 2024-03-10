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
Agar 1-yanvar seshanba bo`lsa, kiritilgan k - kun haftaning qaysi
kuniga to`g`ri kelishini aniqlovchi dastur tuzilsin;
09.03.2024
"""

k = input("\nYilning nechanchi kuni ekanligini kiriting: ")

try:
    k = int(k)
except:
    natija = "\nNoto`g`ri qiymat kiritldi!\n"
else:
    if 0 < k < 367:
        hafta_k = [
            "dushanba",
            "seshanba",
            "chorshanba",
            "payshanba",
            "juma",
            "shanba",
        ]

        natija = f"1-kuni seshanbadan boshlanadigan yilning {k} kuni, haftaning {hafta_k[k%7]} kuniga to`g`ri keladi!\n"
    else:
        natija = "\nNoto`g`ri qiymat kiritldi!\n"

print(natija)
