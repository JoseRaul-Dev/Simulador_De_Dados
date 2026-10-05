# Simulador de Dados
Simulador de dados desarrollado en Python utilizando la librería **Rich** para implementar una animación al tirar los dados.

## Descripción
Este programa permite al usuario seleccionar diferentes tipos de dados y después elegir los dados que quiera tirar, hasta un máximo permitido.
Al finalizar, se muestra el resultado de cada dado, el total obtenido y el promedio de la tirada.

## Funcionalidades
- Menú principal.
- Selección del tipo de dado (D4, D6, D8, D10, D12 y D20).
- Selección de la cantidad de dados (hasta un máximo).
- Validación de los datos introducidos por el usuario.
- Animación del lanzamiento mediante `Live` y `Panel`.
- Resultado de cada dado mostrado con diferentes colores.
- Cálculo del total de la tirada.
- Cálculo del promedio.
- Control de errores mediante excepciones.
- Opción para añadir estadísticas que se añadirá en el futuro.

## Colores de los resultados
Los resultados se muestran utilizando diferentes colores:
- **Rojo:** cuando el resultado es `1`.
- **Verde:** cuando se obtiene el valor máximo del dado.
- **Amarillo:** para cualquier otro resultado.

## Autor
**Realizado por José Raúl Álvarez**
