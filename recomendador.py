import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

print("🎬 Sistema de Recomendación Básico\n")

# 1️⃣ Datos simulados
datos = {
    "Matrix": [5, 4, 0],
    "Titanic": [2, 1, 5],
    "Avatar": [0, 5, 4]
}

usuarios = ["Lucas", "Ana", "Pedro"]

df = pd.DataFrame(datos, index=usuarios)

print("📊 Tabla de puntuaciones:")
print(df)

# 2️⃣ Calcular similitud entre usuarios
similitud = cosine_similarity(df)

df_similitud = pd.DataFrame(similitud, index=usuarios, columns=usuarios)

print("\n🔍 Similitud entre usuarios:")
print(df_similitud)

# 3️⃣ Buscar el usuario más parecido a Lucas
usuario_objetivo = "Lucas"
similares = df_similitud[usuario_objetivo].sort_values(ascending=False)

print("\n👥 Usuarios más similares a Lucas:")
print(similares)

# 4️⃣ Recomendar película a Lucas

# Películas que Lucas no vio (tienen 0)
peliculas_no_vistas = df.loc["Lucas"] == 0

# Películas que Ana vio y Lucas no
recomendaciones = df.loc["Ana"][peliculas_no_vistas]

print("\n🎥 Películas recomendadas para Lucas:")
print(recomendaciones)