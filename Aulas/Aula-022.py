#Modularização

#Surgiu no incicio da década de 60
#Sistemas ficando cada vez maior
#Foco:dividir um programa grande 
#Foco:aumentar a legibilidade
#Foco:facilitar a manutenção
#Vantagens 
#Organização do codigo
#Facilide na manutenção
#Ovultação de Código detalhado
#Reutilização em outros projetos

#import Uteis as u
#from Uteis import fatorial , dobro

from modulos import numeros as n

num=int(input("Digite um valor "))
fat = n.fatorial(num) 


print(f'O fatorial de {num} é {fat}')
print(f'O dobro do número {num} e {n.dobro(num)} ')
print(f'O triplo do número {num} e {n.triplo(num)}')







