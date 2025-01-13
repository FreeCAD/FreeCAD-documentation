# Drawing Workbench/es
<div class="mw-translate-fuzzy">





</div>


**The '''Drawing Workbench''' is no longer included after version 0.20.<br>
The [TechDraw Workbench](TechDraw_Workbench.md) is its more advanced replacement.**

<img alt="El icono del Ambiente de trabajo Dibujar" src=images/Workbench_Drawing.svg  style="width:128px;">



## Introducción

El módulo de Dibujo le permite poner su trabajo 3D en papel. Es decir, poner vistas de tus modelos en una ventana 2D e insertar esa ventana en un dibujo, por ejemplo una hoja con un borde, un título y tu logo y finalmente imprimir esa hoja.




<img alt="" src=images/Drawing_extraction.png  style="width:600px;">



## Herramientas

Estas son las herramientas para la creación, configuración y exportación de hojas de dibujo 2D

-   <img alt="" src=images/Drawing_New.png  style="width:32px;"> [Abre SVG scalable vector graphic](Drawing_Open_SVG/es.md): Abre una hoja de dibujo previamente guardada en un archivo SVG

-   <img alt="" src=images/Drawing_Landscape_A3.png  style="width:32px;"> [Nueva hoja de dibujo en formato A3](Drawing_Landscape_A3/es.md): Crea una hoja de dibujo nueva a partir de la plantilla por defecto A3 de FreeCAD

-   <img alt="" src=images/Drawing_View.png  style="width:32px;"> [Insertar una vista](Drawing_View/es.md): Inserta una vista de los objetos seleccionados en la hoja de dibujo activa

-   <img alt="" src=images/Drawing_Annotation.png  style="width:32px;"> [Anotación](Drawing_Annotation/es.md): Añade una anotación a la hoja de dibujo actual

-   <img alt="" src=images/Drawing_Clip.png  style="width:32px;"> [Clip](Drawing_Clip.md): Adds a clip group to the current drawing sheet

-   <img alt="" src=images/Drawing_Openbrowser.png  style="width:32px;"> [Open Browser](Drawing_Openbrowser.md): Opens a preview of the current sheet in the browser

-   <img alt="" src=images/Drawing_Orthoviews.png  style="width:32px;"> [Ortho Views](Drawing_Orthoviews.md): Automatically creates orthographic views of an object on the current drawing sheet

-   <img alt="" src=images/Drawing_Symbol.png  style="width:32px;"> [Symbol](Drawing_Symbol.md): Adds the contents of a SVG file as a symbol on the current drawing sheet

-   <img alt="" src=images/Drawing_DraftView.png  style="width:32px;"> [Draft View](Draft_Drawing.md): Inserts a special Draft view of the selected object in the current drawing sheet

-   <img alt="" src=images/Drawing_SpreadsheetView.png  style="width:32px;"> [Spreadsheet View](Drawing_SpreadsheetView.md): Inserts a view of a selected spreadsheet in the current drawing sheet

-   <img alt="" src=images/Drawing_Save.png  style="width:32px;"> [Guardar hoja de dibujo](Drawing_Save/es.md): Guarda la hoja de dibujo actual como un archivo SVG

-   [Project Shape](Drawing_ProjectShape.md): Creates a projection of the selected object (Source) in the 3D view.

-    **Nota**
    

La herramienta [Borrador boceto](Draft_Drawing/es.md) es utilizada para [ objetos boceto](Draft_Workbench/es.md). Tiene algunas capacidades adicionales sobre las herramientas de Dibujo, y soporta objetos específicos como [Dimensiones de borrador](Draft_Dimension/es.md).

## Flujo de trabajo 

El documento contiene un objeto de forma 3D (pierna) del que queremos producir un dibujo. Por lo tanto, se crea una \"Página\". Una página es instanciada desde una plantilla, por ejemplo, la plantilla \"A3_Landscape\". La plantilla es un documento [SVG](SVG/es.md) que puede contener un marco de página, un logotipo y otros elementos.

En esta página podemos insertar una o varias vistas. Cada vista tiene una posición en la página, un factor de escala y propiedades adicionales. Cada vez que la página o la vista o el objeto referenciado cambian, la página se regenera y la visualización de la página se actualiza.



## Guión

Por el momento, el flujo de trabajo de la interfaz gráfica de usuario es muy limitado, por lo que la API de scripting es más interesante.

See the [Drawing API example](Drawing_API_example.md) page for a description of the functions used to create drawing pages and views.



## Ampliación del módulo dibujo 

Some notes on the programming side of the drawing module will be added to the [Drawing Documentation](Drawing_Documentation.md) page. This is to help quickly understand how the drawing module works, enabling programmers to rapidly start programming for it.

## External links 


<div class="mw-translate-fuzzy">

## Enlaces externos 

-   [Introducción al dibujo mecánico en Youtube - por el Universo Normal](https://www.youtube.com/watch?v=1Hm5Zyjmjac)


</div>


<div class="mw-translate-fuzzy">





</div>


{{Drawing Tools navi

}}



---
⏵ [documentation index](../README.md) > [Obsolete Workbenches](Category_Obsolete Workbenches.md) > [Drawing](Category_Drawing.md) > Drawing Workbench/es
