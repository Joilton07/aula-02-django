import config

run = True
notas = []
users = []
aprovacao = [
    "Aprovado",
    "Reprovado",
    "Nota Máxima"
]
i = 1
soma = 0
l = 0


while run:
    
    command = input("command >> ")

    if command == "exit":
        run = False
    
    if command == "new user":

        names = ""
        qtde_notas = 0
        notas = []
        nota = 0
        soma = 0
        media = 0
        i = 1

        names = input("Nome: ")
        qtde_notas = int(input("Quantidade de notas: "))
        
        while i <= qtde_notas:
            nota = float(input(f"Nota {i}: "))
            if nota > config.nota_minima and nota < config.nota_maxima:
                notas.append(nota)
                soma = soma + nota
                i += 1
            else: 
                print("Erro! Nota inválida")
        
        media = soma / qtde_notas
        if media < config.media_global:
            aprova = aprovacao[1]
        elif media < config.nota_maxima:
            aprova = aprovacao[0]
        else:
            aprova = aprovacao[2]
            
        
        users.append({"Name": names, "Notas": notas, "Media": media, "Aprovacao": aprova})   
        
    if command == "list users":
        for user in users:
            print(user)
    
    if command == "show user":
        index = int(input("Index: "))
        print(users[index])
    
    l += 1