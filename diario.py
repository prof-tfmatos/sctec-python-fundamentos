with open("diario.txt", "a", encoding="utf-8") as arquivo:
   arquivo.write("Dia4 - Aprendendo a manipular arquivos com o Python. Função open com argumentos r, w & a \n")
   arquivo.write("Dia5 - Seria interessante expandir esse código com um input no terminal para digitar a frase do dia. \n")

with open("diario.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())