weight = int(input("Weight: "))
unit = input("(L)bs or (K)gs")
if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"You are {converted} kilos")
elif unit.upper() == 'K':
    converted = weight / 0.45
    print(f"You are {converted} pounds")
else:
    print("Please input K or L")