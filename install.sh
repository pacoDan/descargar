#!/bin/bash

# Crear el entorno virtual
python -m venv env
# if [ $? -ne 0 ]; then
#   echo "Error al crear el entorno virtual"
#   exit 1
# fi

# Activar el entorno virtual
source env/bin/activate
# if [ $? -ne 0 ]; then
#   echo "Error al activar el entorno virtual"
#   exit 1
# fi

# Instalar las dependencias del archivo requirements.txt
pip install -r requirements.txt
# if [ $? -ne 0 ]; then
#   echo "Error al instalar las dependencias"
#   exit 1
# fi
echo "Actualizando pip!!"
pip install --upgrade pip

# Paso 5: Generar el ejecutable con PyInstaller
echo "Generando el ejecutable..."
pyinstaller --onefile descargar.py

echo "Se genero el ejecutable correctamente"

mkdir -p ~/miBinDaniel && cp dist/descargar ~/miBinDaniel/

# Agregar el directorio al PATH en .bashrc y .zshrc si no está ya presente
if ! grep -q 'export PATH="$HOME/miBinDaniel:$PATH"' ~/.bashrc; then
  echo 'export PATH="$HOME/miBinDaniel:$PATH"' >>~/.bashrc
fi

if ! grep -q 'export PATH="$HOME/miBinDaniel:$PATH"' ~/.zshrc; then
  echo 'export PATH="$HOME/miBinDaniel:$PATH"' >>~/.zshrc
fi

# Recargar los archivos de configuración de la terminal
source ~/.bashrc
source ~/.zshrc

echo "El ejecutable se ha agregado al PATH y la terminal se ha actualizado."
