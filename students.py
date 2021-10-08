import config

qtde_notas = int(input("Quantidade de notas: "))
alunos = []
notas = []
i = 1
soma = 0

nome = input("Nome do aluno: ")
alunos.append({"name": nome, "notas": []})

while i <= qtde_notas:
    nota = float(input(f"Nota {i}: "))
    if nota > config.nota_minima and nota < config.nota_maxima:
        notas.append(nota)
        soma = soma + nota
        i += 1
    else: 
        print("Erro! Nota inválida")

alunos[0]["notas"] = notas
media = soma / qtde_notas

if media < config.media_global:
    print("Reprovado")
elif media < config.nota_maxima:
    print("Aprovado")
else:
    print("Nota máxima")

print("As notas digitadas foramm: ")
for aluno in alunos:
    print(aluno)