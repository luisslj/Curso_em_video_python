dig = input('Digite algo :')

print(f'Só tem espaços{dig.isspace}')
print(f'O tipo digitado {type(dig)}')
print(f'É alfanumerico? {dig.isalpha()}')
print(f'É um numero? {dig.isalnum()}')
print(f'Está em maiuscula? {dig.isupper()}')
print(f'Está em minuscula? {dig.islower()}')
print(f'Está capitalizada? {dig.capitalize()}')