temp = input("Digite la hora y minutos actuales (formato de 24 horas): ")
hora, mins = temp.split(":")
hora = float(hora)
mins = float(mins)
mins = (mins/60)
hora += mins
if hora >= 7 or hora <= 8 :
    val = "Es hora de desayunar"
elif hora >= 12 or hora <= 13 :
    val = "Es hora de almorzar"
elif hora >= 18 or hora <= 19 :
    val = "Es hora de cenar"
print(val)