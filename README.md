Este proyecto implementa un sistema simple de recomendación de películas basado en similitud entre usuarios.

 ¿Cómo funciona?

1. Se crea una tabla de usuarios con puntuaciones de películas.
2. Se calcula la similitud entre usuarios usando **Cosine Similarity**.
3. Se identifica el usuario más parecido.
4. Se recomienda una película que el usuario similar haya visto y el usuario objetivo no.

 Tecnologías utilizadas

- Python
- pandas
- scikit-learn
- cosine_similarity

 Cómo ejecutarlo

1. Instalar dependencias:

pip install pandas scikit-learn

2. Ejecutar:

python recomendador.py

 Ejemplo de lógica

Si dos usuarios tienen gustos similares y uno vio una película que el otro no, el sistema la recomienda.

---

Proyecto educativo para aprender fundamentos de sistemas de recomendación y filtrado colaborativo.
