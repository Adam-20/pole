předměty = ["tělocvik", "Německý jazyk" ,"počítačové sítě", "český jazyk", "hardware"]
print(len(předměty))
for i in předměty:
    print(i)
dalsiPredmet = input("zadejte dalsi predmet")
předměty.append(dalsiPredmet)
předměty.remove(2)
předměty.sort()
print(předměty.reverse())