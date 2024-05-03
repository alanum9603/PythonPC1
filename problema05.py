shows = int(input("Digite cuantos shows musicales ha visto en el último año: "))
if shows < 0 :
    print("La cantidad no puede ser negativa")
elif shows > 3 :
    val = True
    print(val)
else : 
    val = False
    print(val)