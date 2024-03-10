"""
Masala: Hafta kunlari quyidagicha tartibda berilgan:
0 - yakshanba
1 - dushanba
2 - seshanba
3 - chorshanba
4 - payshanba
5 - juma
6 - shanba
[1 ; 366] oralig`ida yotuvchi k soni berilgan.
Agar 1-yanvar dushanba bo`lsa, kiritilgan k - kun haftaning qaysi
kuniga to`g`ri kelishini aniqlovchi dastur tuzilsin;

09.03.2024
"""

k = input("\nYilning nechanchi kuni ekanligini kiriting: ")
try:
    k = int(k)
except:
    natija = "\nNoto`g`ri qiymat kiritildi!\n"
else:
    if 0 < k < 367:
        hafta_kunlari = [
            "yakshanba",
            "dushanba",
            "seshanba",
            "chorshanba",
            "payshanba",
            "juma",
            "shanba",
        ]
        natija = f"1-kuni Dushanbadan boshlanadigan yilning {k} kuni hafatning {hafta_kunlari[k%7] } kuniga to`g`ri keladi.\n"
    else:
        natija = "\nNoto`g`ri qiymat kiritildi!\n"

print(natija)
