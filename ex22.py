#código python que verifica se um nome é ALUNO
nome=input("Qual o seu nome? ")
sobrenome=input("Digite o sobrenome ")
nome=nome.upper()
sobrenome=sobrenome.upper()
# .upper() função que transforma tudo que foi colocado em maiúsculo
if nome == "SENAC" and sobrenome == "SANTA LUZIA":
    print(f"OLÁ {nome} {sobrenome}")
else:
    print("Você não é aluno do SENAC")