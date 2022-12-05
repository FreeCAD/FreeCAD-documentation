# OpenSCAD Workbench/es
<div class="mw-translate-fuzzy">





</div>

<img alt="El icono del Ambiente de trabajo OpenSCAD" src=images/Workbench_OpenSCAD.svg  style="width:128px;">

## Introducción

El <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:24px;"> [Ambiente de trabajo OpenSCAD](OpenSCAD_Workbench/es.md) tiene como objetivo ofrecer interoperabilidad con el software de código abierto [OpenSCAD](http://www.openscad.org/). Este programa no se distribuye como parte de FreeCAD, pero debe ser instalado para hacer uso completo de este banco de trabajo. No se debe confundir OpenSCAD con [OpenCASCADE](OpenCASCADE/es.md), que es el núcleo geométrico que FreeCAD utiliza para construir la geometría en la pantalla. Las bibliotecas de OpenCASCADE siempre son necesarias para usar FreeCAD, mientras que el ejecutable de OpenSCAD es totalmente opcional.

Contiene un [importador](OpenSCAD_CSG/es.md) que permite abrir los archivos CSG de OpenSCAD en FreeCAD, y un exportador para producir un árbol basado en CSG. La geometría que no esté basada en operaciones CSG será exportada como una malla.

Este ambiente de trabajo contiene funciones para modificar el árbol de características CSG y reparar modelos. También contiene herramientas de propósito general que no requieren la instalación de OpenSCAD; se pueden utilizar junto con otros ambientes de trabajo. Por ejemplo, el [ambiente de trabajo Mesh](Mesh_Workbench/es.md) utiliza internamente las funciones de OpenSCAD para realizar operaciones con [meshes](mesh/es.md), ya que son bastante robustas.


{{TOCright}}

![](images/OpenSCADexamaple1.png )

## Dependencias

En FreeCAD 0.19, el módulo Ply (Python-Lex-Yacc), que se utiliza para importar archivos CSG, fue eliminado del código fuente de FreeCAD, ya que es una biblioteca de terceros no desarrollada por FreeCAD. Como resultado, ahora es necesario instalar Ply antes de utilizar el ambiente de trabajo OpenSCAD. Cuando se utiliza una versión estable y pre-empaquetada de FreeCAD esta dependencia debería instalarse automáticamente en todas las plataformas; en otros casos, por ejemplo, cuando se [compila](Compiling/es.md) desde el código fuente, puede que tengas que instalarlo desde un repositorio online.

En openSUSE esto se hace mediante:


```python
sudo zypper install python3-ply
```

En los sistemas basados en Debian/Ubuntu esto se hace de la siguiente manera:


```python
sudo apt install python3-ply
```

La instalación general en todas las plataformas se puede hacer desde el índice de paquetes de Python.


```python
pip3 install --user ply
```

## OpenSCAD lenguaje y formato de archivo 

El lenguaje de OpenSCAD permite la utilización de variables y bucles. Permite especificar submódulos para reutilizar geometría y código. Esta alto grado de flexibilidad hace el análisis sintáctico muy complejo. Actualmente el módulo OpenSCAD en FreeCAD no puede manejar el lenguaje de OpenSCAD de forma nativa. En cambio si OpenSCAD está instalado, se puede utilizar para convertir la entrada en un formato de salida denominado \'CSG\'. Es un subconjunto del lenguaje OpenSCAD y se puede utilizar como la entrada de OpenSCAD para su procesamiento posterior. Durante la conversión todo el comportamiento paramétrico se pierde. Todos los nombres de variables serán desechados, los bucles expandidos y las expresiones matemáticas evaluadas.

## Herramientas

-   <img alt="" src=images/OpenSCAD_ColorCodeShape.svg  style="width:32px;"> [ColorCodeShape](OpenSCAD_ColorCodeShape/es.md): Cambia el color de la selección o todas las formas basadas en su validez
-   <img alt="" src=images/OpenSCAD_ReplaceObject.svg  style="width:32px;"> [Reemplazar objeto](OpenSCAD_ReplaceObject/es.md): Reemplaza una objeto en el árbol de operaciones. Por favor, selecciona los objetos antiguos, nuevos y padres
-   <img alt="" src=images/OpenSCAD_RemoveSubtree.svg  style="width:32px;"> [Eliminar sub-árbol](OpenSCAD_RemoveSubtree/es.md): Elimina los objetos seleccionados y todos sus descendientes que no estén referenciados desde otros objetos
-   <img alt="" src=images/OpenSCAD_RefineShapeFeature.svg  style="width:32px;"> [Refinar operación de forma](OpenSCAD_RefineShapeFeature/es.md): Crea una operación de forma refinada
-   <img alt="" src=images/OpenSCAD_MirrorMeshFeature.svg  style="width:32px;"> [Elemento de malla espejo](OpenSCAD_MirrorMeshFeature/es.md): Crear característica de malla de espejo.
-   <img alt="" src=images/OpenSCAD_ScaleMeshFeature.svg  style="width:32px;"> [Escalar la característica de malla](OpenSCAD_ScaleMeshFeature/es.md): Escala una característica de malla.
-   <img alt="" src=images/OpenSCAD_ResizeMeshFeature.svg  style="width:32px;"> [Redimensionar elemento de malla](OpenSCAD_ResizeMeshFeature/es.md): Cambia el tamaño de una característica de malla.

<img alt="" src=images/OpenSCAD_IncreaseToleranceFeature.svg  style="width:32px;"> [Función de aumento de la tolerancia](OpenSCAD_IncreaseToleranceFeature/es.md): Aumenta la tolerancia de bordes/caras/vértice de objeto(s) seleccionado(s).

-   <img alt="" src=images/OpenSCAD_Edgestofaces.svg  style="width:32px;"> [Aristas a caras](OpenSCAD_Edgestofaces/es.md): Convierte aristas a caras. Útil para preparar geometría DXF importada para su extrusión.
-   <img alt="" src=images/OpenSCAD_ExpandPlacements.svg  style="width:32px;"> [Expandir ubicación](OpenSCAD_ExpandPlacements/es.md): Expande todas las ubicaciones por debajo del árbol de operaciones
-   <img alt="" src=images/OpenSCAD_ExplodeGroup.svg  style="width:32px;"> [Explotar grupo](OpenSCAD_ExplodeGroup.md): explota las partes primitivas fusionadas.
-   <img alt="" src=images/OpenSCAD_AddOpenSCADElement.svg  style="width:32px;"> [Añadir elementos OpenSCAD](OpenSCAD_AddOpenSCADElement/es.md): Añade un elemento OpenSCAD introduciendo código OpenSCAD en el panel de tareas y ejecutando el binario de OpenSCAD (requiere de OpenSCAD)
-   <img alt="" src=images/OpenSCAD_MeshBoolean.svg  style="width:32px;"> [Mesh Booleana](OpenSCAD_MeshBoolean.md): Crea un nuevo objeto de malla mediante una operación booleana a partir de formas.
-   <img alt="" src=images/OpenSCAD_Hull.svg  style="width:32px;"> [Casco](OpenSCAD_Hull/es.md): Aplica un casco a las formas seleccionadas.
-   <img alt="" src=images/OpenSCAD_Minkowski.svg  style="width:32px;"> [Minkowski](OpenSCAD_Minkowski/es.md): Aplica una suma de minkowski a las formas seleccionadas.

## Preferencias

-   <img alt="" src=images/Std_DlgParameter.svg  style="width:32px;"> [Preferencias](OpenSCAD_Preferences/es.md): Preferencias disponibles para las herramientas de OpenSCAD.

## Limitations


<div class="mw-translate-fuzzy">

## Limitaciones

OpenSCAD crea geometría sólida constructiva, así como importa archivos de malla y extruye geometría 2D desde archivos [DXF](DXF/es.md). FreeCAD permite crear CSG con primitivas también.

El núcleo de geometría de FreeCAD (OCCT) funciona trabajando sobre una representación de los limites.

Por tanto la conversión de CSG a BREP en teoría debería ser posible. Mientras que una conversión de BREP a CSG es, en general, imposible.


</div>


<div class="mw-translate-fuzzy">

OpenSCAD funciona internamente sobre mallas. Algunas operaciones que son útiles en mallas no son significativas en un modelo BREP y no pueden ser totalmente compatibles. Entre estos se encuentran el convex hull, minkowski sum, glide y subdiv. Actualmente ejecutamos el binario OpenSCAD para realizar operaciones de hull y minkwoski e importar el resultado. Esto significa que la geometría involucrada será triangulada. En OpenSCAD, a menudo se usa una escala no uniforme, que no impone ningún problema cuando se usan mallas. En nuestra geometría, las primitivas geométricas del núcleo (líneas, secciones circulares, etc.) se convierten a BSpline antes de realizar tales deformaciones. Esas líneas de BS son conocidas por causar problemas en operaciones booleanas posteriores. Una solución automática no está disponible en este momento. Por favor, siéntase libre de publicar en el foro si encuentra tales problemas. A menudo, tales problemas se pueden resolver remodelando piezas pequeñas. Una deformación de un cilindro puede sustituirse por una extrusión de una elipsis.


</div>

## Importing text 

Importing OpenSCAD code with texts requires that the fonts that are used are properly installed on your system. You can verify this by opening OpenSCAD as a standalone tool and checking the list in **Help → Font List**. The list will also give you the correct font names. If a font does not appear in the list after installing, you may have to manually copy the font file to the appropriate system directory.

Importing texts is relatively slow. Behind the scenes FreeCAD uses a DXF file created by OpenSCAD. The more contours there are the slower the import.

It can be a good idea to first import a simple test case (replace {{Incode|NameOfFont}} with the correct font name):

    TESTFONT="NameOfFont";
    linear_extrude(0.001) {
      text("A", size=5, font=TESTFONT, script="Latn");
    };

The {{Incode|<nowiki>script="Latn"</nowiki>}} parameter can be left out here, but is required if the text string does not contain any letters, but only punctuation and/or numbers.

Please note that {{Incode|<nowiki>use <FONT>;</nowiki>}} statements in your source files are ignored when importing in FreeCAD. Under OpenSCAD the effect of a {{Incode|use}} statement is that the provided font file is temporarily added to the list of known fonts (although even there the statement does not work when a script is modified interactively).

## Pistas

Cuando se importa [DXF](DXF/es.md) establecer la precisión Borrador a una cantidad sensible para que afecte a la detección de aristas conectadas.

Si FreeCAD se cuelga importando CSG, es muy recomendable activar *automáticamente comprobar el modelo después de una operación booleana* en **Menú → Editar → Preferencias → DiseñoPiezas → Configuración del modelo**

## Tutoriales

-   [Importar código OpenSCAD](Import_OpenSCAD_code/es.md)

## Enlaces


<div class="mw-translate-fuzzy">

-   Repositorio de código fuente de OpenSCAD en [GitHub](https://github.com/openscad/openscad)
-   [Open tickets tagged \"Openscad\" on the FreeCAD bugtracker](https://freecadweb.org/tracker/search.php?tag_string=OpenSCAD)
-   [Elementos etiquetados con \"Openscad\" en Thingiverse](http://www.thingiverse.com/tag:openscad)


</div>


<div class="mw-translate-fuzzy">





</div>


{{OpenSCAD Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [OpenSCAD](Category_OpenSCAD.md) > OpenSCAD Workbench/es
