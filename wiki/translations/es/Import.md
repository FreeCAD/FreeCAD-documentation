---
- TutorialInfo:/es
   Topic:Ambiente de trabajo Arquitectura
   Level:Avanzado
   Time:120 minutos
   Author:Pablo Gil
   FCVersion:0.19.x
   Files:
}}

## Introducción

Fue una investigación tan dura sobre cómo obtener una copia de trabajo de IfcOpenShell-python en OSX/macOS con el fin de importar/exportar archivos IFC que estoy compartiendo este tutorial en caso de que ayude a más personas. Mi sistema es OSX 10.11.6, 64bits con Python 2.7.11, puede que te funcione si también tienes OSX ya que suelen ser de 64bits pero puede diferir del mío. El procedimiento puede ser muy similar si tienes Linux o Windows pero probablemente tenga algunas diferencias.

## Requisitos

-   [IfcOpenShell](IfcOpenShell/es.md)
-   FreeCAD v0.19 o superior

## Pasos

1\. Descargue o clone el proyecto completo de GitHub en <https://github.com/IfcOpenShell/IfcOpenShell> (siempre será la versión más reciente)

:   
    `git clone https://github.com/IfcOpenShell/IfcOpenShell
---

# Import/Export IFC - compiling IfcOpenShell/es

     

2\. Desde un terminal ve a la carpeta {{FileName|/nix/` y lanza el script. En OSX se ejecuta con: 
```python
cd nix/
./build-all.sh
``` Tardará desde 30 hasta 120 minutos en compilar todo. No es la forma más inteligente de compilar [IfcOpenShell](IfcOpenShell/es.md) pero este sencillo script compilará todas las dependencias, versiones de Python, etc.

3\. Una vez que termine (no recuerdo ahora pero se imprimirá algo como \"Built IfcOpenShell\...\" y volverá a su prompt) tendrás una nueva carpeta {{FileName|/IfcOpenShell/build/}} llena de archivos y carpetas. Por mi experiencia personal, hace dos semanas el script \"build-all.sh\" de nix no terminaba con éxito pero después de probarlo ayer con las últimas actualizaciones funcionó bien así que supongo que podrías experimentar algo similar en caso de que el desarrollo siga adelante\... Así que ahora tienes todo lo que necesitas pero tienes que hacer algo de trabajo manual para que funcione:

4\. Abre FreeCAD y abre la [consola de Python](Python_console/es.md) y la [vista de informe](Report_view/es.md). Luego escribe en la consola de Python lo siguiente: {{Code|código=
importar sys
print sys.path
}} Obtendrás una línea larguísima con todas las rutas que lee FreeCAD. Puedes instalar IfcOpenShell en cualquiera de ellas, pero te sugiero que lo coloques dentro de una en la que encuentres un {{FileName|/site-packages/}} después de un {{FileName|/Python/}} o {{FileName|/python-algo/}}. En mi caso era {{FileName|/Library/Python/2.7/site-packages}}. (Nota: encontrarás rutas dentro del directorio de tu aplicación pero te sugiero que no las uses porque entonces IfcOpenShell sólo estará disponible para esta aplicación)

5\. Una vez localizado donde quieres/tienes que instalarlo, ve allí con tu explorador de archivos (Finder en OSX). Es decir, entra en la carpeta {{FileName|/site-packages/}}

:   
    `cd site-packages/`
    

6\. Abre una nueva ventana del explorador de archivos y navega hasta tu proyecto GitHub descargado: **/IfcOpenShell/src/ifcopenshell-python/** y copia la carpeta completa **/ifcopenshell/**\'.

7\. Pégalo dentro de la carpeta **/site-packages/**. Ahora deberías tener algo como: {{Code|código=
/paquetes-de-sitio/ifcopenshell/__init__.py
/paquetes-de-sitio/ifcopenshell/entity_instance.py
/paquetes-de-sitio/ifcopenshell/file.py
/paquetes del sitio/ifcopenshell/geom/app.py
/paquetes del sitio/ifcopenshell/geom/main.py
/paquetes/ifcopenshell/geom/occ_utils.py
/paquetes web/ifcopenshell/geom/__init__.py
/paquetes del sitio/ifcopenshell/guid.py
}}

8\. Ahora tenemos que elegir a los archivos dentro de la carpeta /build/, son: 
```python
ifcopenshell_wrapper.so
ifcopenshell_wrapper.py
``` pero como lo hemos compilado todo tendrás que elegir el que coincida con tu versión de FreeCAD Python. Compruébalo fácilmente leyendo la primera línea dentro de tu vista de la [Python console/es](Python_console/es.md) de FreeCAD. En mi caso fue Python 2.7.11.

9\. Ahora vamos a copiar los archivos dentro del lugar que corresponde a tu versión de Python. En mi caso fue: 
```python
/IfcOpenShell/build/Darwin/x86_64/build/ifcopenshell/[b]python-2.7[/b].10/ifcwrap/
```

10\. Pégalos dentro de {{FileName|/site-packages/ifcopenshell/}}

11\. Compruebe que todo está en su sitio: 
```python
/site-packages/ifcopenshell/__init__.py                  (1)
/site-packages/ifcopenshell/entity_instance.py           (1)
/site-packages/ifcopenshell/_ifcopenshell_wrapper.so     (2)
/site-packages/ifcopenshell/file.py                      (1)
/site-packages/ifcopenshell/geom/__init__.py             (1)
/site-packages/ifcopenshell/geom/app.py                  (1)
/site-packages/ifcopenshell/geom/main.py                 (1)
/site-packages/ifcopenshell/geom/occ_utils.py            (1)
/site-packages/ifcopenshell/guid.py                      (1)
/site-packages/ifcopenshell/ifcopenshell_wrapper.py      (2)
```

\(1\) desde el proyecto GitHub
(2) desde la carpeta /build/

12\. Cierre y vuelva a abrir FreeCAD

## Pruebas

Ahora que está instalado, vamos a comprobar si todo funciona como se espera:

12.1 en la consola de Python escribir: 
```python
import ifcopenshell
from ifcopenshell import geom
``` si no arroja ningún error significa que puede estar correctamente instalado


<div class="mw-translate-fuzzy">

12.2 Ve al manual de FreeCAD de Yorik, navega a la parte inferior de la página y descarga los siguientes archivos para probar: 
```python
house.FCStd
house.ifc
```


</div>

12.3 Abra {{FileName|house.FCStd}}, seleccione el objeto raíz \"Edificio\" y expórtelo (**Archivo → Exportar**) estableciendo el Tipo de archivo como \"Industry Foundation Classes (\*.ifc)\". Pulsa **Guardar** y si funciona y no lanza un error en la [Report view/es](Report_view/es.md) entonces está funcionando.

12.4 Prueba final, importar {{FileName|house.ifc}} en un nuevo archivo, así que abre un nuevo archivo e importa ese archivo\... tardará un poco.

13\. ¡Disfruta de BIM con FreeCAD!

## Reflexiones finales 

Mi opinión es que FreeCAD debería tener versiones precompiladas de IfcOpenShell junto con la distribución porque construirlo por ti mismo es un dolor total y el usuario medio no lo hará (no saben cómo compilar, gestionar GitHub, etc), pero bueno, tal vez en el futuro.

Espero que te ayude.

Salud

## Enlaces

-   Hilo del foro relacionado [discusión](http://forum.freecadweb.org/viewtopic.php?f=23&t=17536)
-   [IfcOpenShell](IfcOpenShell/es.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [BIM](Category_BIM.md) > [Arch](Category_Arch.md) > [3rd Party](Category_3rd Party.md) > [File_Formats](Category_File_Formats.md) > Import/Export IFC - compiling IfcOpenShell/es
