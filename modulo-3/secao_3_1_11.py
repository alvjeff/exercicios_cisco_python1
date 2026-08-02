income = float(input("Entre com os rendimentos anuais: "))
if income < 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + 0.32*(income - 85528)


tax = round(tax, 0)
print("A taxa é:", tax, "thalers")
