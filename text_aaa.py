repet = "s"
while repet == "s":
    n1 = int(input("Digite um numero: "))
    while 10 >= n1 <=0:
        n1 = int(input("Digite o primeiro número entre 10-0: "))
    n2 = int(input("Digite um numero: "))
    while 10 >= n2 <=0:
        n1 = int(input("Digite o segundo número entre 10-0: "))

    media = (n1+n2)/2
    print(media)
    repet = input("Vc deseja realizar um novo calculo?(s/n)")



