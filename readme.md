```sh
source install.sh
```
```sh
pip install -r requirements
```
--------------------------------------------------

Puedes generar un ejecutable de tu programa Python utilizando herramientas de empaquetado y distribución como PyInstaller, cx_Freeze o py2exe, dependiendo de tus necesidades y plataforma. Aquí te muestro cómo hacerlo con PyInstaller:

Instalar PyInstaller:
Si aún no tienes PyInstaller instalado, puedes instalarlo utilizando pip:
Copy code
pip install pyinstaller
Crear el ejecutable:
Una vez que tengas PyInstaller instalado, dirígete al directorio que contiene tu script de Python y ejecuta el siguiente comando:
css
Copy code
pyinstaller --onefile tu_script.py
Reemplaza tu_script.py con el nombre de tu script de Python. Este comando creará un directorio dist dentro del directorio actual, que contendrá el ejecutable de tu programa.
Ejecutar el programa:
Una vez que se haya completado la generación del ejecutable, puedes encontrarlo en la carpeta dist. Puedes ejecutar este ejecutable en el sistema operativo correspondiente.
El uso de la opción --onefile comprime todo el código y las dependencias en un solo archivo ejecutable, lo que facilita la distribución y el uso del programa en diferentes sistemas. Sin embargo, si prefieres mantener los archivos separados, puedes omitir esta opción.

Recuerda que cuando generas el ejecutable, PyInstaller intentará detectar automáticamente todas las dependencias de tu programa y las incluirá en el ejecutable generado. Sin embargo, es posible que tengas que ajustar manualmente la configuración de PyInstaller si tu programa utiliza módulos externos o recursos adicionales.




