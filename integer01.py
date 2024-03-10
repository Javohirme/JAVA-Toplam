# Masala: Uzunlik l santimetrda berilgan. Undagi to`liq metrlar sonini aniqlovchi dastur tuzilsin;
l = input("\nUzunlikni sm da kiriting: ")

try:
    l = float(l)
except:
    natija = "\nNoto`g`ri qiymat kiritildi!\n"
else:
    if l >= 0:
        m = l // 100
        natija = f"\n{l} sm uzunlikda {int(m)} metr mavjud."
    else:
        natija = "\nNoto`g`ri qiymat kiritildi!\n"

print(natija)
