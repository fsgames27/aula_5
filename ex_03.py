n= float(input("Quantos alunos a na sala?"))
soma = 0
i=0
while i<n:
    ler = float(input("me diga as notas: "))
    soma += ler
    i+=1
media = soma/i
print(f"A media é: {media:.1f}")