def calcular_peso_en_otro_planeta(peso_tierra, gravedad_planeta):
    peso_otro_planeta = peso_tierra * gravedad_planeta / 9.8
    return peso_otro_planeta

# Peso en la Tierra (en kilogramos)
peso_tierra = float(input("Ingresa el peso en la Tierra (en kg): "))

# Calcular peso en la Luna
gravedad_luna = 1.622  # gravedad en la Luna en m/s^2
peso_luna = calcular_peso_en_otro_planeta(peso_tierra, gravedad_luna)
print("El peso en la Luna es:", peso_luna, "kg")

# Calcular peso en Marte
gravedad_marte = 3.71  # gravedad en Marte en m/s^2
peso_marte = calcular_peso_en_otro_planeta(peso_tierra, gravedad_marte)
print("El peso en Marte es:", peso_marte, "kg")
