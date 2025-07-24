import os

# Carpetas a revisar
folders = ['Tensorflow/workspace/images/train', 'Tensorflow/workspace/images/test']

# Texto a reemplazar
original = '<name>Sí</name>'
reemplazo = '<name>Si</name>'

for folder in folders:
    if not os.path.exists(folder):
        print(f"Carpeta no encontrada: {folder}")
        continue

    print(f"\nProcesando archivos en: {folder}")
    
    for filename in os.listdir(folder):
        if filename.endswith('.xml'):
            path = os.path.join(folder, filename)

            with open(path, 'r', encoding='utf-8') as file:
                contenido = file.read()

            if original in contenido:
                contenido = contenido.replace(original, reemplazo)
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(contenido)
                print(f"✔️ Corregido: {filename}")
            else:
                print(f"— Sin cambios: {filename}")
