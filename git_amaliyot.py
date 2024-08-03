#"raqamlar” nomli tekst fayl ichiga 1 dan 10 gacha 
sonlarni kiritib, ularning yig'indisini ekranga 
chiqaruvchi dastur yarating.

with open("raqamlar.txt","wt") as f:
    f.write("1 2 3 4 5 6 7 8 9 10")

with open("raqamlar.txt","rt") as g:
    data = g.read().split()
    ls = []
    for x in data:
            ls.append(int(x))
    sum = 0
    for x in ls:
        sum += x
    print(sum)    
