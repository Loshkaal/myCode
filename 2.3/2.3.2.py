stroks = 0
while ( hare := str(input())) != 'Приехали!':
    if "зайка" in hare:
        stroks += 1
print(stroks)