import math


class ConversorAngulos:
    def __init__(self, valor, tipo):
        self.valor = valor
        self.tipo = tipo

    def convertir_a_radianes(self):
        if self.tipo == "grados":
            return self.valor * math.pi / 180
        else:
            return self.valor

    def convertir_a_grados(self):
        if self.tipo == "radianes":
            return self.valor * 180 / math.pi
        else:
            return self.valor


# Solicitar entrada de usuario
valor = float(input("Ingresa el valor del ángulo: "))
tipo = input("Ingresa el tipo (grados/radianes): ").lower()

# Crear instancia de la clase con los valores ingresados
conversor = ConversorAngulos(valor, tipo)

# Realizar la conversión según el tipo ingresado
if tipo == "grados":
    resultado = conversor.convertir_a_radianes()
    print(f"{valor} grados es igual a {resultado:.2f} radianes")
elif tipo == "radianes":
    resultado = conversor.convertir_a_grados()
    print(f"{valor} radianes es igual a {resultado:.2f} grados")
else:
    print("Tipo no reconocido. Por favor, ingresa 'grados' o 'radianes'.")
