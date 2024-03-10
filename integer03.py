"""
Masala: Faylning hajmi baytlarda berilgan.
Bo`lib, butunni olish operatoridan foydalanib fayl hajmini
to`liq kilobaytlarda ifodalovchi dastur tuzilsin;
05.03.2024
"""

b = input("\nFaylning hajmini baytlarda kiriting: ")
try:
    b = float(b)
except:
    natija = "\nNoto`g`ri qiymat kiritildi!\n"
else:
    if b >= 0:
        natija = f"{b} bayt {int(b/1024)} kb bo`ladi."
    else:
        natija = "\nNoto`g`ri qiymat kiritildi!\n"
print(natija)
