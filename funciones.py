# Creación de función para calcular el área de un rectangulo
def area_rectangulo (base, altura):
    if base >= 0 and altura >= 0:
        area = base * altura
        print(f"El área del rectangulo es {area}") 
    else:
        print ("Numeros invalidos")

#Ejemplo de uso de la funcioón creada
area_rectangulo(3,8)
