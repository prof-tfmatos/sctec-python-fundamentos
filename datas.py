from datetime import date, datetime

texto = input("Data de nascimento (dd/mm/aaaa): ")
nascimento = datetime.strptime(texto, "%d/%m/%Y").date()
print(nascimento)

hoje = date.today()

dias = (hoje - nascimento).days
idade =dias // 365
print("Você tem aproximadamente", idade, "anos.")

nomes = {
    0: "segunda-feira",
    1: "terça-feira",
    2: "quarta-feira",
    3: "quinta-feira",
    4: "sexta-feira",
    5: "sábado",
    6: "domingo",
}
print("Dia da semana em que você nasceu:", nomes[nascimento.weekday()])
natal = date(hoje.year, 12, 25)
if natal < hoje:
    natal = date(hoje.year + 1, 12, 25)
print("Faltam", (natal - hoje).days, "dias para o próximo Natal.")