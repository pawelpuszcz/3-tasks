'''
ZADANIE 3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5, DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL.
'''
start = 2
stop = 5.5
step = 0.5

def ListGenerator(start, stop, step):
    numbers = []
    i = start
    while i <= stop:
        numbers.append(i)
        i += step
    return numbers

print(ListGenerator(start, stop, step))
 