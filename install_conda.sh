#!/bin/bash

# Nombre del entorno a crear
NOMBRE_ENV="env_descargar13"

# Crear el entorno Conda y aceptar automáticamente todas las confirmaciones
conda create -n $NOMBRE_ENV -y

# Inicializar Conda en el script
eval "$(~/miniconda3/bin/conda shell.bash hook)"

# Activar el entorno
conda activate $NOMBRE_ENV

# Confirmar que el entorno está activado
echo "El entorno '$NOMBRE_ENV' ha sido creado y activado automáticamente."

# Añadir aquí otros comandos necesarios
