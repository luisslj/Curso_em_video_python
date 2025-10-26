# + Adição 
# - Subutração
# * Multiplicação
# / Divição
# ** Potencia 
# // Divição interia 
# % Resto da divisão

# ordem de precedência
# 1 ()
# 2 **
# 3 *,/,//,%
# 4 + -

#5 + 2 ==
#5 - 2 ==
#5 * 2 ==
#5 / 2 ==
#5 ** 2 ==
#5 // 2 ==
#5 % 2 ==

a = float(5)
b = float(2)

c = a + b
print(c)
c = a - b
print(c)
c = a * b
print(c)
c = a / b
print(c)
c = a ** b
print(c)
c = a // b
print(c)
c = a % b
print(c)


n1 = int (input('Digite um número!'))
n2 = int (input('Digite outro número!'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 % n2

print ('A soma é {}, \n o produto é {}' \
'e a divisão é {:.3}'.format (s, m, d), end='')
print('Divisão inteiira {} e potencia {}'.format(di, e))

