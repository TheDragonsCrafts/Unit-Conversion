# Importar el módulo locale para dar formato a la salida
import locale

# Establecer el idioma y la moneda locales
locale.setlocale(locale.LC_ALL, 'es_MX.UTF-8')

# Definir una función genérica que convierta entre dos monedas
def convertir_moneda(cantidad, tasa):
    return cantidad * tasa

# Definir una función que muestre el menú al usuario y devuelva la opción elegida
def mostrar_menu():
    # Definir una lista para almacenar las opciones del menú
    opciones = []
    
    # Usar un bucle for para generar las opciones del menú a partir del diccionario de tasas
    for origen in tasas:
        for destino in tasas[origen]:
            opciones.append(f"{len(opciones) + 1}. Convertir de {origen} a {destino}")
    
    # Agregar la opción de salir al final de la lista
    opciones.append(f"{len(opciones) + 1}. Salir")
    
    # Mostrar las opciones del menú
    for opcion in opciones:
        print(opcion)
    
    # Solicitar al usuario que ingrese el número de la opción que desea
    opcion = input("Ingrese el número de la opción que desea: ")
    
    # Devolver la opción elegida
    return opcion

# Definir una función que valide la entrada del usuario y devuelva un valor numérico positivo
def validar_entrada(mensaje):
    # Usar un bucle while para repetir hasta obtener una entrada válida
    while True:
        # Solicitar al usuario que ingrese un valor
        valor = input(mensaje)
        
        # Usar un try-except para manejar posibles errores de entrada
        try:
            # Convertir el valor a un número flotante
            valor = float(valor)
            
            # Validar que el valor sea positivo
            if valor > 0:
                # Devolver el valor válido
                return valor
            else:
                # Mostrar un mensaje de error y repetir el bucle
                print("Error: el valor debe ser positivo.")
        except ValueError:
            # Mostrar un mensaje de error y repetir el bucle
            print("Error: el valor debe ser numérico.")

# Definir un diccionario con las tasas de cambio entre las monedas disponibles
tasas = {
    "Dólar": {
        "Peso": 18.4902,
        "Euro": 0.84,
        "Yen": 111.07
    },
    "Peso": {
        "Dólar": 0.0541,
        "Euro": 0.0468,
        "Yen": 6.21
    },
    "Euro": {
        "Dólar": 1.19,
        "Peso": 21.37,
        "Yen": 131.98
    },
    "Yen": {
        "Dólar": 0.0090,
        "Peso": 0.16,
        "Euro": 0.0076
    }
}

while True:
    print("Bienvenido al conversor de moneda!")
    
    # Llamar a la función que muestra el menú al usuario y obtener la opción elegida
    opcion = mostrar_menu()
    
    try:
        # Convertir la opción a un número entero
        opcion = int(opcion)
        
        # Validar que la opción sea válida
        if opcion in range(1, len(tasas) ** 2 + 1):
            # Obtener la moneda origen y destino según la opción elegida
            origen, destino = list(tasas.keys())[int((opcion - 1) / len(tasas))], list(tasas.keys())[(opcion - 1) % len(tasas)]
            
            # Llamar a la función que valida la entrada del usuario y obtener la cantidad de la moneda origen que desea convertir
            cantidad = validar_entrada(f"Ingrese la cantidad de {origen}s que desea convertir a {destino}s: ")
            
            # Obtener la tasa de cambio correspondiente a la opción elegida
            tasa = tasas[origen][destino]
            
            # Llamar a la función de conversión con la cantidad y la tasa correspondiente
            resultado = convertir_moneda(cantidad, tasa)
            
            # Dar formato a la salida con el separador de miles y dos decimales
            cantidad = locale.format_string("%.2f", cantidad, grouping=True)
            resultado = locale.format_string("%.2f", resultado, grouping=True)
            
            # Mostrar el resultado al usuario
            print(f"{cantidad} {origen}s son {resultado} {destino}s")
            
            # Preguntar al usuario si desea hacer la conversión inversa
            respuesta = input(f"¿Desea convertir {resultado} {destino}s a {origen}s? (S/N): ")
            
            # Validar que la respuesta sea válida
            if respuesta.upper() == "S":
                # Llamar a la función de conversión con el resultado y la tasa inversa
                inverso = convertir_moneda(float(resultado.replace(",", "")), 1 / tasa)
                
                # Dar formato a la salida con el separador de miles y dos decimales
                inverso = locale.format_string("%.2f", inverso, grouping=True)
                
                # Mostrar el resultado al usuario
                print(f"{resultado} {destino}s son {inverso} {origen}s")
 
        elif opcion == len(tasas) ** 2 + 1:
            print("¡Hasta luego!")
            break
 
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")
 
    except (ValueError, TypeError):
        print("Error de entrada. Por favor, ingrese un valor numérico.")