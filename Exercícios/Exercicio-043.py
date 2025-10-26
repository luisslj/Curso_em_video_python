'''Dedenvolva uma lógica que leia o peso e altura de uma pessoa, 
calcule sei IMC e mostre seu status, de acordo com a tabela a abaixo:'''
# -Abaixo de 18.5:Abaixo do peso
# -Entre 18.5 e 25:peso ideal
# -25 até 30:Sobrepeso
# -30 até 40:Obesidade
# -Acima de 40:Obsidade mórbida
'''Se uma pessoa pesa 70 kg e mede 1,75 m, o cálculo seria:
70 / (1,75 * 1,75) = 22,86
Portanto, o IMC dessa pessoa é 22,86'''

altura = float (input('Digite sua altura: '))
peso = float (input('Digite seu peso: '))
imc = peso / (altura * altura)


if imc <= 18.5:
    print(f'Está a baixo do peso seu imc e de {imc:.2f}')# -Abaixo de 18.5:Abaixo do peso
elif imc > 18.5 and imc < 25:
    print(f'Está com o peso ideal seu imc e de {imc:.2f}')# -Entre 18.5 e 25:peso ideal
elif imc > 25 and imc < 30: 
    print(f'Esta com sobrepeso seu imc é de {imc:.2f}')# -25 até 30:Sobrepeso
elif imc > 30 and imc < 40:
    print(f'Está com Obsidade seu imc é de {imc:.2f}')# -30 até 40:Obesidade
elif imc > 40:
    print  (f'Está com obsidade mórbida seu imc é de {imc:.2f}') # -Acima de 40:Obsidade mórbida 

    


