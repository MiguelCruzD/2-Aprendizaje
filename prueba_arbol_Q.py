import utileria as ut
import arboles_cualitativos as ac
import os
import random

# Ruta del archivo de datos
archivo_datos = os.path.join("iris", "iris.data")
atributos = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
target = 'class'

# Verifica si el archivo existe
if not os.path.exists(archivo_datos):
    raise FileNotFoundError(f"No se encontró el archivo: {archivo_datos}")

# Lee los datos desde el archivo CSV
# Asegúrate de que 'ut.lee_csv' esté correctamente implementada
datos = ut.lee_csv(
    archivo_datos, 
    atributos=atributos,  # Usamos la variable atributos en lugar de hardcodear
    separador=',', 
    tiene_encabezado=False  # Este parámetro es importante si el archivo no tiene encabezado
)

# Aleatoriza y divide los datos en entrenamiento y validación
random.seed(42)
random.shuffle(datos)  # Mezclamos los datos para evitar sesgos
N = int(0.8 * len(datos))  # 80% para entrenamiento, 20% para validación
datos_entrenamiento = datos[:N]
datos_validacion = datos[N:]

# Lista para almacenar los errores
errores = []

# Entrena el árbol con diferentes profundidades y evalúa
for profundidad in [1, 3, 5, None]:
    arbol = ac.entrena_arbol(
        datos_entrenamiento, 
        target, 
        atributos, 
        max_profundidad=profundidad
    )
    
    # Evaluación en el conjunto de entrenamiento y validación
    error_en_muestra = ac.evalua_arbol(arbol, datos_entrenamiento, target)
    error_en_validacion = ac.evalua_arbol(arbol, datos_validacion, target)
    
    # Guardamos los resultados
    errores.append((profundidad, error_en_muestra, error_en_validacion))

# Muestra los resultados de los errores
print(f"{'Profundidad'.center(12)}{'Ein'.center(12)}{'E_out'.center(12)}")
print("-" * 40)
for profundidad, error_entrenamiento, error_validacion in errores:
    print(f"{str(profundidad).center(12)}"
      f"{error_entrenamiento:.4f}".center(12) +
      f"{error_validacion:.4f}".center(12))
print("-" * 40)

# Entrenamos un árbol con toda la data y lo imprimimos
arbol_final = ac.entrena_arbol(datos, target, atributos, max_profundidad=3)
ac.imprime_arbol(arbol_final)
