import csv
lista = []
with open("notas.csv", newline="", encoding="utf-8") as f:
    for aluno in csv.DictReader(f):
        media = (float(aluno["nota1"]) + float(aluno["nota2"])) / 2
        if media >= 7:
            situacao = "Aprovado"
        else:
            situacao = "Reprovado"
        lista.append({"nome": aluno["nome"], "media": media, "situacao":situacao})

with open("resultado.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.DictWriter(f, fieldnames=["nome", "media", "situacao"])
    escritor.writeheader()
    escritor.writerows(lista)