'''
ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n. NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE
1-n = [1,2,3,4,5,...,10]
np. n=10
wejście: [2,3,7,4,9], 10
wyjście: [1,5,6,8,10]

'''

input = [2,3,7,4,9]
n = 10

def MissingElements(input, n):
    output = []
    for i in range(1,n+1):
        if i not in input:
            output.append(i)
    return output

