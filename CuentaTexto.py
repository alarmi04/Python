try:    
    texto = input("Introduce un texto: ")
    vecesAparece = texto.upper().count("PYTHON")
    print(f"Python aparece {vecesAparece} veces")
except Exception as e:
    print("Error", str(e))