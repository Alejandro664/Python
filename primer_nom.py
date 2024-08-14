def primer_nombre(nombre):
    a = 0
    b = 2
    c = 1

    name = nombre[a:b]
    name2 = nombre[c:b]

    while name2 != " ":
        a = 0
        b += 1
        c += 1
        name = nombre[a:b]
        name2 = nombre[c:b]
        
    return name