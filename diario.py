with open("diario.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Meu querido diário: escrever código na mão é divertido, mas doloroso. \n")

with open("diario.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())