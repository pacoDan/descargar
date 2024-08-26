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

echo "Todo se ha ejecutado correctamente"
