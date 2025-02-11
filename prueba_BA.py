import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

# Cargar el conjunto de datos Iris
iris_data = load_iris()
X = iris_data.data  # Características
y = iris_data.target  # Etiquetas

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Parámetros a probar
n_est_values = [10, 50, 100, 200]
max_depth_values = [None, 5, 10, 20]
max_features_values = [None, 'sqrt', 'log2']

# Arreglo para almacenar resultados
results = []

# Entrenar el modelo con diferentes combinaciones de parámetros
for n_est in n_est_values:
    for max_depth in max_depth_values:
        for max_features in max_features_values:
            rf = RandomForestClassifier(n_estimators=n_est, max_depth=max_depth, max_features=max_features, random_state=42)
            rf.fit(X_train, y_train)
            y_pred = rf.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            results.append((n_est, max_depth, max_features, accuracy))

# Convertir los resultados en un DataFrame
results_df = pd.DataFrame(results, columns=['n_est', 'max_depth', 'max_features', 'accuracy'])

# Mostrar el DataFrame con los resultados
print(results_df)

# Visualización de la precisión según los parámetros max_depth (profundidad maxima) y n_est (n estimada)
pivot_table = results_df.pivot_table(values='accuracy', index='n_est', columns='max_depth')

plt.figure(figsize=(10, 6))
plt.title('Precisión del modelo con diferentes valores de n_est y max_depth')
sns.heatmap(pivot_table, annot=True, cmap='coolwarm', cbar_kws={'label': 'Precisión'})
plt.ylabel('Número de árboles (n_est)')
plt.xlabel('Profundidad máxima (max_depth)')
plt.show()

# Analizar el efecto de max_features (numero maximo de caracteristicas) en el rendimiento
plt.figure(figsize=(10, 6))
for max_features in max_features_values:
    filtered_results = results_df[results_df['max_features'] == max_features]
    plt.plot(filtered_results['n_est'], filtered_results['accuracy'], label=f'max_features={max_features}')
    
plt.title('Efecto de max_features en la precisión')
plt.xlabel('Número de árboles (n_est)')
plt.ylabel('Precisión')
plt.legend()
plt.grid(True)
plt.show()
