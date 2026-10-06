# Aula 3 do Módulo 04 (02/10/2026) · Mãos à obra + commit: mini banco de dados de alunos (slide 123)
#
# 1. Crie uma lista com pelo menos 4 dicionários, cada um representando
#    um aluno (nome e nota).
# 2. Use um for com if para imprimir apenas os alunos aprovados (nota >= 7).
# 3. Adicione um contador para exibir, ao final, quantos alunos foram
#    aprovados no total.
# 4. Commit (mensagem descritiva) e push para o GitHub.

alunos = [
    {"nome": "Ana", "nota": 9.0},
    {"nome": "Bruno", "nota": 6.5},
    {"nome": "Carla", "nota": 7.0},
    {"nome": "Diego", "nota": 5.0},
]

aprovados = 0
for aluno in alunos:
    if aluno["nota"] >=7:
        print(aluno["nome"], aluno["nota"])
        aprovados += 1

print("Total de aprovados:", aprovados)