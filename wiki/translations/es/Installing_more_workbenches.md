# Installing more workbenches/es
## Introducción

Desde la v0.17 es fácil añadir [ambientes de trabajo externos](external_workbenches/es.md) utilizando el [Gestor de complementos](Std_AddonMgr/es.md). Un usuario normal no necesita hacer más que usar esta herramienta.

Siga leyendo para obtener más información sobre la instalación de ambientes de trabajo.

## Descripción general 

Los ambientes de trabajo no son más que colecciones de archivos que se colocan en una carpeta. Esta carpeta suele estar comprimida en un archivo zip. En la instalación, esta carpeta simplemente se descomprime y se copia en 
```python
$ROOT_DIR/Mod/
``` donde `$ROOT_DIR` es un directorio de nivel superior buscado por FreeCAD al iniciarse. Esto es esencialmente lo que hace el [Gestor de complementos ](Std_AddonMgr/es.md).

Los directorios `Mod/` se escanean cada vez que se inicia FreeCAD, y los ambientes de trabajo disponibles se añaden automáticamente.

## Instalación de todo el sistema 

Los ambientess de trabajo instalados de esta manera estarán disponibles para todos los usuarios. Dependiendo de su sistema, es posible que necesite privilegios de administrador para acceder al directorio de instalación.

Copie la carpeta del ambiente de trabajo en `$INSTALL_DIR/Mod/`, donde `$INSTALL_DIR` es el directorio de instalación de FreeCAD.

-   En Linux suele ser `/usr/share/freecad/Mod/`
-   En Windows suele ser `C:\\Program Files\FreeCAD\Mod`
-   En macOS suele ser `/Applications/FreeCAD/Mod/`

## Instalación para un solo usuario 

Los ambientes de trabajo instalados de esta manera estarán disponibles sólo para un usuario, pero no requerirán ningún privilegio de administrador.

Copiar la carpeta del ambiente de trabajo en `$USER_DIR/Mod/`, donde `$USER_DIR` es el directorio de FreeCAD para un `username` particular.

-   En Linux es normalmente `/home/username/.FreeCAD/Mod/`.
-   En Windows es `%APPDATA%\FreeCAD\Mod`, que suele ser `C:\Users\''username''\Appdata\Roaming\FreeCAD\Mod`.
-   En macOS suele ser `/Users/username/Library/Preferences/FreeCAD/Mod/`. Una forma de llegar al directorio de preferencias es utilizar el elemento de menú del \"Finder\" **Ir → Ir a la carpeta**, e introducir `~/Librería/Preferencias/FreeCAD`.

## Información adicional 

Puedes encontrar información adicional sobre cómo crear un ambiente de trabajo personalizado en el [Centro de usuarios avanzados](Power_users_hub/es.md) y en el [Centro de desarrolladores](Developer_hub/es.md).

Consulta también una descripción detallada en la página [cómo instalar ambientes de trabajo adicionales](How_to_install_additional_workbenches/es.md).


{{Powerdocnavi

}} 

_

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Installing more workbenches/es
