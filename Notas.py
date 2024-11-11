nota1 = int(input("Primera nota: "))
nota2 = int(input("Segunda nota: "))
nota3 = int(input("Tercera nota: "))

if nota1 < 4 and nota2 < 4 and nota3 < 4:
    print("Tu nota final es un 0.")
elif nota1 > 4 and nota2 > 4 and nota3 > 4:
    notaFinal = (nota1*0.30) + (nota2*0.20) + (nota3*0.50)
    print(f"Tu nota final es {notaFinal}")
elif nota1 > 4 or nota2 > 4 or nota3 > 4:
    print("Tu nota final es un 2.")