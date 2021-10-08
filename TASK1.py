'''
ZADANIE 1. GENERATOR KODÓW POCZTOWYCH
przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi

'''

s1 = "79-900"
s2 = "80-155"

def CodeGenerator(s1, s2):
    codes_list = [f'79-{i}' for i in range(901,1000)] + [f'80-00{i}' for i in range(0,10)] + [f'80-0{i}' for i in range(10,100)] + [f'80-{i}' for i in range(100,155)]
    code_generator = (n for n in codes_list)
    return code_generator

