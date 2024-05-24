"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String

Em Python string é tudo que estiver entre:

- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Joao Silva'
- Aspas duplas -> "Joao Silva"
- Aspas simples triplas -> '''Joao Silva'''
"""

# - Aspas duplas triplas -> """Joao Silva""

# Entrada de dados
# print("Qual seu nome? ")
nome = input('Qual seu nome? ') # input -> entrada

# Exemplo de print 'antigo' versão 2.x
# print('Seja bem-vindo(a) %s' % nome)

#Exemplo de print 'moderno'3.x
# print ('Seja bem-vindo(a) {0}' .format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem-vindo(a) {nome}')

# print('Qual a sua idade? ')
idade = int(input('Qual a sua idade? '))


# Processamento

# Saída
# Exemplo de print 'antigo' versão 2.x
# print('A(O) %s tem %s anos' % (nome, idade))

# Exemplo de print 'mais atual' 3.7
print(f'A(O) {nome} tem {idade} anos')

# Cast é a 'conversão de um tipo de dado para outro.

print(f'A(O) {nome} nasceu em {2022 - idade}')