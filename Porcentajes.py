chicas = int(input("Cuantas chicas hay en clase: "))
chicos = int(input("Cuantos chicos hay en clase: "))
total = chicos + chicas
porcentajeChicos = (chicos/total)*100
porcentajeChicas = (chicas/total)*100

print(f"Un {porcentajeChicos}%% de personas son chicos y un {porcentajeChicas}%% son chicas")