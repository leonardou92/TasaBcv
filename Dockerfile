# Usa una imagen base de Python
FROM python:3.12-slim

# Configura el directorio de trabajo
WORKDIR /app

# Copia los archivos de tu aplicación al contenedor
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY templates/ templates/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que la aplicación se ejecutará
EXPOSE 5000

# Define el comando para ejecutar la aplicación
CMD ["python", "app.py"]
