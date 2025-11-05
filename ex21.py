#código python que verifica se um nome é ALUNO
nome=input("Qual o seu nome? ")
nome=nome.upper()
# .upper() função que transforma tudo que foi colocado em maiúsculo
if nome == "ALUNO":
    print(f"Olá {nome}")
else:
    print("Você não é aluno do SENAC")