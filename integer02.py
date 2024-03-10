# Og`irlik m kilogramda berilgan. Undagi to`liq tonnalar sonini aniqlovchi dastur tuzilsin; 05.03.2024
m = input("\nOg`irlikni kiriting: ")
try:
    m = float(m)
except:
    natija = "\nNoto`g`ri qiymat kiritildi.\n"
else:
    t = m // 10 ** (3)
    if m >= 0:
        natija = f"{m} kg og`irlikda {int(t)} tonna mavjud."
    else:
        natija = "\nNoto`g`ri qiymat kiritildi.\n"
print(natija)
