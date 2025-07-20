Aquí tienes una lista de comandos fructíferos e importantes en Vim y Neovim que son especialmente útiles para el desarrollo de software:
Claro, aquí tienes los comandos para deshacer y rehacer en Vim y Neovim:
- **Deshacer**: `u`
- **Rehacer**: `Ctrl + r`
### 👉 Atajos por defecto:
- `gcc` → comenta/descomenta una línea
- `gc` en visual mode → comenta bloque seleccionado
Estos comandos te permiten revertir cambios y volver a aplicarlos, lo que es muy útil durante la edición de texto y el desarrollo de software.
Aquí tienes un resumen de los comandos para guardar cambios en Neovim:
1. **:w**: Guarda el archivo actual sin salir de Neovim.
2. **:wq**: Guarda el archivo y cierra Neovim.
3. **:x**: Guarda el archivo y cierra Neovim, solo si hay cambios.
4. **:w!**: Fuerza el guardado del archivo, incluso si fue abierto en modo solo lectura.
### Comandos de Navegación
- **Moverse a la siguiente palabra**: `w`
- **Moverse a la palabra anterior**: `b`
- **Moverse a la siguiente línea**: `j`
- **Moverse a la línea anterior**: `k`
- **Ir al inicio de la línea**: `0`
- **Ir al final de la línea**: `$`
- **Ir a la siguiente ocurrencia de búsqueda**: `n`
- **Ir a la ocurrencia anterior de búsqueda**: `N`
### Comandos de Edición
- **Entrar en modo de inserción**: `i` (antes del cursor), `a` (después del cursor)
- **Salir del modo de inserción**: `Esc`
- **Copiar línea actual**: `yy`
- **Cortar línea actual**: `dd`
- **Pegar**: `p` (después del cursor), `P` (antes del cursor)
- **Deshacer**: `u`
- **Rehacer**: `Ctrl + r`
- **Eliminar palabra**: `dw`
- **Eliminar hasta el final de la línea**: `d$`
### Comandos de Selección
- **Seleccionar texto**: `v` (modo visual), `V` (modo visual de línea), `Ctrl + v` (modo visual en bloque)
- **Copiar texto seleccionado**: `y` (yank)
- **Cortar texto seleccionado**: `d` (delete)
### Comandos de Búsqueda y Reemplazo

- **Buscar texto**: `/texto_a_buscar` y presiona `Enter`
- **Reemplazar texto**: `:%s/texto_a_buscar/texto_nuevo/g` para reemplazar en todo el archivo
### Comandos de Manejo de Archivos
- **Guardar cambios**: `:w`
- **Salir**: `:q`
- **Guardar y salir**: `:wq` o `ZZ`
- **Abrir un archivo**: `:e nombre_del_archivo`
- **Cerrar el archivo actual**: `:bd`
### Comandos de Ventanas

- **Dividir ventana horizontalmente**: `:split`
- **Dividir ventana verticalmente**: `:vsplit`
- **Navegar entre ventanas**: `Ctrl + w` seguido de `h`, `j`, `k`, o `l`

### Comandos de Portapapeles

- **Copiar al portapapeles del sistema**: `"+y` (para copiar) y `"+p` (para pegar)

### Comandos de Configuración

- **Mostrar número de línea**: `:set number`
- **Activar resaltado de sintaxis**: `:syntax on`
- **Activar auto-indentación**: `:set autoindent`

### Comandos de Compilación y Ejecución

- **Ejecutar un comando externo**: `:!comando`
- **Compilar y ejecutar código**: Puedes usar `:!gcc % -o output && ./output` para compilar y ejecutar un archivo C, por ejemplo.

Estos comandos son esenciales para mejorar la productividad y eficiencia al desarrollar software en Vim y Neovim. Con el tiempo y la práctica, te familiarizarás con ellos y podrás utilizarlos de manera más efectiva.
