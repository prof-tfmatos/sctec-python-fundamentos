import csv
import re

with open("contatos.csv", newline="", encoding="utf-8") as f:
    for contato in csv.DictReader(f):
        digitos = re.sub(r"\D", "", contato["telefone"])
        if re.fullmatch(r"\d{11}", digitos):
            situacao = "válido"
        else:
            situacao = "inválido"
        print(contato["nome"], digitos, situacao)