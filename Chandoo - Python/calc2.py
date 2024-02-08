exp = []
stopped = False
while not stopped:
    e = int(input("Enter the expenses: (Type 0 to stop)"))
    if e != 0:
        exp.append(e)
    else:
        stopped = True
total = sum(exp) 
print("The sum of expenses are "+ str(total))
print("The expenses are "+ str(exp))
print("The maximum spent is "+ str(max(exp)))
print("The minimum spent is "+ str(min(exp)))