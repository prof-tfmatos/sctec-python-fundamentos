"""Lista e append

Exercício da Aula 2 do Módulo de Python (2026/10/02).
SCTEC · Machine Learning e Visão Computacional, turma T4.
Professor: André Dienes . Referência: slide 100.

O que o enunciado pede:
lista de 5+ itens; append, remove/pop, sort; imprimir cada etapa. 
"""
autores = [ "Camões", "Pessoa", "Tolentino", "Azevedo", "Augusto"]

print(autores[0])
print(autores[1])
print(autores[2])

autores.append("Gregório")
autores.remove("Tolentino")
autores.pop(2)
autores.sort()


print(autores)
