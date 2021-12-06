total = 0 

for i in range(1, 1000):
    if i % 3 == 0:
        total += i
        print(f"[{i}] is a Multiple of 3")
    elif i % 5 == 0:
        total += i
        print(f"[{i}] is a Multiple of 5")
    else:
        print(f"[{i}] is not a Multiple of 3 or 5")
   
print(f"Total Sum: [{total}]")
