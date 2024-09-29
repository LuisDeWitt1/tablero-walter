import streamlit as st

# 1.Función de saludo simple
def saludar(nombre):
    return f"Hola, {nombre}!"

# 2.Suma de dos números
def sumar(a, b):
    return a + b

# 3.Area de un triángulo
def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

# 4. Calculadora de descuento
def calcular_precio_final(precio, descuento=10, impuesto=16):
    precio_con_descuento = precio - (precio * descuento / 100)
    precio_final = precio_con_descuento + (precio_con_descuento * impuesto / 100)
    return precio_final

# 5.Suma de una lista de números
def sumar_lista(numeros):
    return sum(numeros)

# 6.Funciones con valores predeterminados
def producto(nombre_producto, cantidad=1, precio_unitario=10):
    return cantidad * precio_unitario

# 7.Numeros pares e impares
def numeros_pares_e_impares(numeros):
    pares = [num for num in numeros if num % 2 == 0]
    impares = [num for num in numeros if num % 2 != 0]
    return pares, impares

# 8.Multiplicacion con *args
def multiplicar_todos(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

# 9.Informacion de una persona con **kwargs
def informacion_personal(**kwargs):
    return "\n".join(f"{clave}: {valor}" for clave, valor in kwargs.items())

# 10.Calculadora flexible
def calculadora_flexible(a, b, operacion='suma'):
    if operacion == 'suma':
        return a + b
    elif operacion == 'resta':
        return a - b
    elif operacion == 'multiplicación':
        return a * b
    elif operacion == 'división':
        return a / b
    else:
        return "Operación no válida"

#Aplicación Streamlit
st.title("Tablero Interactivo de Walter")

#Sidebar para selección de ejercicios
exercise = st.sidebar.selectbox("Selecciona un ejercicio", range(1, 11))

if exercise == 1:
    nombre = st.text_input("Ingresa tu nombre:")
    if st.button("Saludar"):
        st.write(saludar(nombre))

elif exercise == 2:
    num1 = st.number_input("Ingresa el primer número:", step=1, value=0)
    num2 = st.number_input("Ingresa el segundo número:", step=1, value=0)
    if st.button("Sumar"):
        st.write("Resultado:", sumar(num1, num2))

elif exercise == 3:
    base = st.number_input("Ingresa la base del triángulo:", step=1.0, value=0.0)
    altura = st.number_input("Ingresa la altura del triángulo:", step=1.0, value=0.0)
    if st.button("Calcular Área"):
        st.write("Área del triángulo:", calcular_area_triangulo(base, altura))

elif exercise == 4:
    precio = st.number_input("Ingresa el precio original:", step=1.0, value=0.0)
    descuento = st.number_input("Ingresa el porcentaje de descuento:", step=1, value=10)
    impuesto = st.number_input("Ingresa el porcentaje de impuesto:", step=1, value=16)
    if st.button("Calcular Precio Final"):
        st.write("Precio Final:", calcular_precio_final(precio, descuento, impuesto))

elif exercise == 5:
    numeros = st.text_input("Ingresa una lista de números (separados por comas):")
    if st.button("Sumar Lista"):
        lista_numeros = [int(num) for num in numeros.split(",")]
        st.write("Suma de la lista:", sumar_lista(lista_numeros))

elif exercise == 6:
    nombre_producto = st.text_input("Nombre del producto:")
    cantidad = st.number_input("Cantidad:", step=1, value=1)
    precio_unitario = st.number_input("Precio unitario:", step=1.0, value=10.0)
    if st.button("Calcular Precio Total"):
        st.write("Precio Total:", producto(nombre_producto, cantidad, precio_unitario))

elif exercise == 7:
    numeros = st.text_input("Ingresa una lista de números (separados por comas):")
    if st.button("Separar Pares e Impares"):
        lista_numeros = [int(num) for num in numeros.split(",")]
        pares, impares = numeros_pares_e_impares(lista_numeros)
        st.write("Números Pares:", pares)
        st.write("Números Impares:", impares)

elif exercise == 8:
    numeros = st.text_input("Ingresa una lista de números (separados por comas):")
    if st.button("Multiplicar Todos"):
        lista_numeros = [int(num) for num in numeros.split(",")]
        st.write("Resultado de la multiplicación:", multiplicar_todos(*lista_numeros))

elif exercise == 9:
    nombre = st.text_input("Nombre:")
    edad = st.number_input("Edad:", step=1, value=0)
    direccion = st.text_input("Dirección:")
    if st.button("Mostrar Información"):
        st.write(informacion_personal(nombre=nombre, edad=edad, direccion=direccion))

elif exercise == 10:
    num1 = st.number_input("Ingresa el primer número:", step=1, value=0)
    num2 = st.number_input("Ingresa el segundo número:", step=1, value=0)
    operacion = st.selectbox("Selecciona una operación:", ["suma", "resta", "multiplicación", "división"])
    if st.button("Calcular"):
        st.write("Resultado:", calculadora_flexible(num1, num2, operacion))
