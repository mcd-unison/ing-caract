## Analizando un grupo de WhatsApp

1. **Descargar los datos de un grupo de WhatsApp.** En la aplicación de WhatsApp, abrir el grupo que se desea analizar, dar clic en el nombre del grupo, bajar hasta la opción "Exportar chat" y elegir "Sin archivos". Esto genera un archivo de texto con todo el historial del grupo.
2. **Ingesta y limpieza de datos**. Leer el archivo de texto en Python y limpiarlo para obtener un DataFrame con las siguientes columnas, además de las columnas que consideres necesarias para el análisis::
   - Fecha y hora del mensaje
   - Nombre del usuario que envió el mensaje (anonimizarlo con nombres de personajes de ficción)
   - Contenido del mensaje
   - Tipo de mensaje (texto, imagen, video, etc.)
   - Número de palabras en el mensaje
3. **Análisis exploratorio de datos**. Realizar un análisis exploratorio de los datos, incluyendo:
   - Estadísticas descriptivas (número total de mensajes, número de usuarios, promedio de mensajes por usuario, etc.)
   - Una nube de palabras con las palabras más frecuentes en los mensajes de texto (¿Como se habla en este grupo?).
   - Una gráfica de barras que muestre quienes son los usuarios más actvos (¿Quienes son los que más escriben?)
   - Una gráfica que muestre la distribución de los mensajes a lo largo del día (¿A qué horas se envían más mensajes?)
   - Una gráfica que muestre la cantidad de mensajes por día de la semana (¿Qué días son los más activos?)
   - Una gráfica que muestre la relación de los usuarios entre mensajes de texto y otro tipo de textos, como imágenes o *stickers* (¿Quíen genera la conversación y quien la estimula?)
4. **Otros análisis**. Realizar otros análisis que consideres interesantes, lo dejamos a tu imaginación, pero que intenten contestar otras dos preguntas sobre el grupo.

Realizar todo en una libreta de Jupyter, ejecutarla y subirla a tu repositorio de GitHub **sin subir los archivos de datos**. Así podemos ver los resultados (anonimizados) y el código que usaste para llegar a ellos, si los datos. Que la libreta *Jupyter* se vea bien, con títulos, subtítulos y comentarios que expliquen lo que estás haciendo.

Para anonimizar y extraer información de los mensajes, por favor usa expresiones regulares tanto como te sea posible. No importa que en este proyecto abuses de las expresiones regulares, es para que practiques su uso.