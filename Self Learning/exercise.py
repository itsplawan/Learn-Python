wt = int(input("Enter your weight: "))
unit = str(input(f'Is it (K)gs or (L)bs? '))

if unit.upper() == "K":
    wt = wt * 2.205
    print(f'Your weight in pounds(lbs) is {wt}')
elif unit.upper() == "L":
    wt = (wt / 2.205)
    print(f'Your weight in Kilograms(kgs) is {wt}')
else:
    print(f'Invalid Entry, please try again. Type K for kilograms and L for pounds for your entered weight: ')
