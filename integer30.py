"""
Masala: Qaysidir yil berilgan. Berilgan yilning qaysi
yuz yillikka kirishini aniqlovchi dastur tuzilsin;
10.03.2024
"""

yil = input("\nYilni kiriting: ")
try:
    yil = int(yil)
except:
    natija = "\nNoto`g`ri qiymat kiritildi!\n"
else:
    if yil > 0:
        asr = yil // 100
        asr += 1
        natija = f"\n{yil}-yil {asr}-asrga tegishli yil bo`lib hisoblanadi."
    else:
        natija = "\nNoto`g`ri qiymat kiritildi!\n"

print(natija)

"""
1-asr
[1;100]

2-asr
[101;200]
"""
