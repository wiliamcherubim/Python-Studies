"""
def executar_busca_linear(lista, valor):
    for elemento in lista:
        if valor == elemento:
            return True
        return False

texto = 'Aprendendo Python na disciplina de linguagem de programação.'

print(f'Tamanho do texto = {len(texto)}')
print(f"Python in texto = {'Wiliam' in texto}")
print(f"Quantidade de y no texto = {texto.count('y')}")
print(f'As 5 primeiras letras são: {texto[0:6]}')

"""

import numpy

matriz_1_1 = numpy.array([1, 2, 3])
matriz_2_2 = numpy.array([[1, 2], [3, 4]])
matriz_3_2 = numpy.array([[1, 2], [3, 4], [5, 6]])
matriz_2_3 = numpy.array([[1, 2, 3], [4, 5, 6]])

print(type(matriz_1_1))
print('\n matriz_1_1 = ', matriz_1_1)
print('\n matriz_2_2 = ', matriz_2_2)
print('\n matriz_3_2 = ', matriz_3_2)
print('\n matriz_2_3 = ', matriz_2_3)


