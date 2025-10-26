from random import randint

num1 = randint(1,9)
num2 = randint(1,9)


cont1 = 0
cont2 = 0

while True:
    s1 = int(input('Digite um número: '))
    s2 = int(input('Digit outro número: '))
    while num1 != s1:
        num1 = randint(1,9)
        cont1 += 1
        print(cont1)
    print(num1)
    while num2 != s2:
        num2 = randint(1,9)
        cont2 += 1
        print(cont2)
    print(num2)
    if s1 == num1 and s2 == num2:
        print(s1,s2)
        break


