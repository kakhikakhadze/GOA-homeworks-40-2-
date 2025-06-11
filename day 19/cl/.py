def luris_sashualo(n):
    luris_racxvebi = [i for i in range(0, n+1) if i % 2 == 0]
    if luris_racxvebi:
        sashualo = sum(luris_racxvebi) / len(luris_racxvebi)
        return sashualo
    else:
        return 0
ricxvi = int(input("შეიყვანეთ რიცხვი: "))
print("ლუწი რიცხვების საშუალო არის:", luris_sashualo(ricxvi))
    