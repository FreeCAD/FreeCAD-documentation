---
- GuiCommand   */es
   Name   *WebTools Git‏‎
   Name/es   *HerramientasWeb Git
   MenuLocation   *HerramientasWeb → Git
   Workbenches   *[HerramientasWeb](WebTools_Workbench/es.md)
   Version   *0.17
---

# WebTools Git/es


<div class="mw-translate-fuzzy">


**A partir de FreeCAD v0.17, esta herramienta ha sido eliminada del Ambiente de trabajos Arquitectura y ahora forma parte del [Ambiente de trabajos HerramientasWeb](WebTools_Workbench/es.md) externo que puedes instalar a través del menú Herramientas → <img src="images/AddonManager.svg" width=24px> [Administrador de complementos](Std_AddonMgr/es.md).
**


</div>

## Descripción

Este comando permite gestionar el documento actual con [GIT](https   *//es.wikipedia.org/wiki/Git). GIT es un potente sistema de control de versiones de archivos, que puede gestionar diferentes versiones de archivos y hacer un seguimiento de los cambios.

Git es una herramienta compleja, considere la posibilidad de aprender los fundamentos de la misma antes de utilizar esta herramienta, para evitar operaciones erróneas que pueden causar la pérdida de datos. Hay una abundante literatura sobre GIT disponible y fácil de encontrar en Internet.

Requisito   **\' Para poder utilizar este comando, el paquete [gitpython](https   *//github.com/gitpython-developers/GitPython) debe estar instalado en tu sistema. En la mayoría de las distribuciones de linux, gitpython está disponible en los repositorios de software estándar como*gitpython*o*python-git\'\'.

## Utilización

1.  Asegúrate de que la [Vista de informe](Report_view/es.md) está abierta ya que los mensajes Git se imprimirán allí.
2.  Guarda el documento activo actual asegurándote de que el archivo guardado está dentro de un repositorio git existente. Puede estar en un subdirectorio.
3.  Seleccionar el menú **HerramientasWeb → <img src="images/WebTools_Git.svg" width=16px> [Git](WebTools_Git/es.md)
**
4.  Esto abre un [Panel de tareas](Task_panel/es.md) en la [Vista combo](Combo_view/es.md).

## Opciones

![Pestaña de tareas que muestra interfaz Git](images/Arch_Git_panel.jpg )

-   El botón **Registro** abrirá un diálogo mostrando las entradas de registro más recientes. La salida corresponde a git log.
-   El botón **Refrescar** volverá a escanear el repositorio en busca de archivos modificados. Después de guardar su trabajo tiene que hacer un refresco manual.
-   El botón **Diff** mostrará las diferencias entre la versión actual de un archivo seleccionado y la versión más reciente almacenada en el repositorio. La salida corresponde a git diff.
    -   Por defecto se hace un diff binario, hay que configurar la herramienta fcinfo para hacer un diff textual.
-   El botón **Seleccionar todo** seleccionará todos los archivos a ser confirmados.
-   El botón **Confirmar** confirmará los archivos seleccionados. Asegúrese de escribir un mensaje de confirmación que describa los cambios que está confirmando.
-   El botón **Pull** descargará cualquier nuevo cambio en el repositorio desde el remoto seleccionado. Si el archivo actualmente abierto en FreeCAD está siendo modificado por un pull, un mensaje de advertencia te informará para que puedas guardar el archivo de nuevo o guardarlo en otro lugar.
-   El botón **Empujar** subirá su(s) última(s) confirmación(es) al remoto seleccionado.

## Limitaciones

-   La herramienta no puede crear nuevos repositorios todavía. Debe tener un repositorio local ya creado. (FreeCAD comprobará si el archivo del documento actual está dentro de un repositorio Git).
-   La herramienta no puede cambiar o crear ramas. Debes hacerlo manualmente con las herramientas Git estándar.

## Habilitación de diffs legibles por humanos para archivos FCStd con la utilidad fcinfo 

El [Formato de archivo FCStd](File_Format_FCStd/es.md) de FreeCAD es un formato binario basado en zip, para el que Git no puede producir diffs adecuados. Esto significa que no puedes ver lo que ha cambiado entre una versión y otra, y también que cada nueva versión almacenada en el repositorio Git es una copia completa del archivo.

Aunque el segundo problema actualmente no tiene solución, el primero puede ser resuelto con una pequeña herramienta disponible en el código fuente de FreeCAD, llamada [fcinfo](https   *//github.com/FreeCAD/FreeCAD/blob/master/src/Tools/fcinfo). Se le puede decir a Git que utilice la utilidad fcinfo para imprimir un informe amigable de un archivo FCStd, y, cuando se le pida que produzca una diferencia entre dos archivos FCStd, producirá una diferencia entre los dos informes fcinfo en su lugar. Tenga en cuenta que esto es sólo un informe visual, una copia completa del archivo seguirá siendo almacenada internamente.

Ejemplo de un diff producido con fcinfo   *


```python
diff --git a/testhouse.FcStd b/testhouse.FcStd
index 08077b6..985b1d8 100644
--- a/testhouse.FcStd
+++ b/testhouse.FcStd
@@ -1,26 +1,25 @@
-Document   * /tmp/43un09_testhouse.FcStd (442K)
-   SHA1   * 67c1985a45d93cba57d5bf44490897aba460100d
+Document   * /tmp/zfXoDd_testhouse.FcStd (370K)
+   SHA1   * db1cb5fca18af7bfdca849028f40550df4d845cb
    Comment    * This is a test house to showcase FreeCAD's BIM worflow and IFC export capabilities
    Company    * uncreated.net
    CreatedBy    * Yorik van Havre
    CreationDate    * Fri May  9 12   *05   *54 2014 
    FileVersion    * 1
    Id    * 
-   Label    * testhouse
-   LastModifiedBy    * Yorik van Havre
-   LastModifiedDate    * 2016-06-28T17   *05   *57-03   *00
+   Label    * testhouse2
+   LastModifiedBy    * Yorik van Havre
+   LastModifiedDate    * Sat Sep 13 20   *46   *36 2014
+
    License    * CC-BY 3.0
    LicenseURL    * http   *//creativecommons.org/licenses/by/3.0/
-   ProgramVersion    * 0.17R7800 (Git)
-   TipName    * 
+   ProgramVersion    * 0.15R3989 (Git)
    Uid    * 67e62d8a-6674-4358-92fe-615443be887a
-   Objects   * (231)
+   Objects   * (221)
        Annotation    * Drawing   *   *FeatureViewAnnotation
        Annotation001    * Drawing   *   *FeatureViewAnnotation
        Annotation002    * Drawing   *   *FeatureViewAnnotation
        Annotation003    * Drawing   *   *FeatureViewAnnotation
-       Annotation004    * Drawing   *   *FeatureViewAnnotation
-       Annotation005    * Drawing   *   *FeatureViewAnnotation
        Array    * Part   *   *FeaturePython (9K)
        Box    * Part   *   *Box (2K)
        Building    * App   *   *DocumentObjectGroupPython
@@ -110,7 +109,7 @@ Document   * /tmp/43un09_testhouse.FcStd (442K)
        Floor    * App   *   *DocumentObjectGroupPython
        Floor001    * App   *   *DocumentObjectGroupPython
        Floor002    * App   *   *DocumentObjectGroupPython
-       Frame    * Part   *   *FeaturePython (89K)
```

Cada archivo de FreeCAD contiene un número de suma de comprobación SHA1, que cambiará cada vez que se guarde el archivo, incluso si no se ha cambiado el contenido. Así que fcinfo siempre imprimirá algo, sin importar los cambios en el contenido.

Para habilitar el uso de fcinfo (sólo para Linux y Mac - PARAHACER   * añadir instrucciones para Windows)

1.  Guarda el archivo fcinfo en algún lugar de la ruta de tu sistema
2.  Hazlo ejecutable
3.  Crea un archivo .gitattributes en tu repositorio Git y añade la siguiente línea en él   *

 *.FCStd diff=fcinfo

Añade las siguientes líneas al archivo .gitconfig en tu directorio principal   *

 [diff "fcinfo"]
 textconv = /ruta/a/fcinfo

Alternativamente, si quieres invocar fcinfo con argumentos (por ejemplo, --gui) utiliza este enfoque [1](https   *//stackoverflow.com/questions/55601430/how-to-pass-a-filename-argument-gitconfig-diff-textconv)   *

 [diff "fcinfo"]
 textconv = sh -c '/ruta/a/fcinfo --gui "$0"'



---
![](images/Right_arrow.png) [documentation index](../README.md) > WebTools Git/es
