weight=float(input("Enter your weight:  "))
unit=input("L(bs) or K(g): ")
if unit.upper=='L':
    weight=weight*0.45
    print(f"You are {weight} kilos")
else:
    weight=weight/0.45
    print(f"You are {weight} pounds")
