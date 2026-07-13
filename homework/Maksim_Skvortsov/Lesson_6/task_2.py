massiv = []
for i in range(1, 101):
    if i % 15 == 0:
        massiv.append("FuzzBuzz")
    elif i % 3 == 0:
        massiv.append("Fuzz")
    elif i % 5 == 0:
        massiv.append("Buzz")
    else:
        massiv.append(i)
print(*massiv, sep='\n')
