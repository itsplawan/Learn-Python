exp = -1
total = 0
maxexp  = 0
minexp = 0
while exp != 0:
    exp = float(input("What is the expenditure? (Type 0 to stop)"))
    total = total + exp
    if maxexp < exp:
        maxexp = exp
    if exp < minexp and exp != 0 and exp >0:
        minexp = exp
print("The expenditure is "+ str(total))
print("The maximum you spent is expenditure "+ str(maxexp))
print("The minimum you spent is expenditure "+ str(minexp))
