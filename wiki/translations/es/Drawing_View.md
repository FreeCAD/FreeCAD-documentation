# Drawing View/es
---
- GuiCommand:   Name: Drawing View   Name/es: Drawing View   Workbenches: Drawing Workbench/es   Dibujo, Complete---


</div>

Esta herramienta crea una nueva vista de los objetos seleccionados en la hoja de dibujo activa.

<img alt="A drawing sheet with three views: front, top and isometric." src=images/Drawing_Views.png  style="width:500px;">


<div class="mw-translate-fuzzy">

### Cómo se utiliza 

Selecciona un objeto en la vista 3D o en el árbol del Proyecto, luego pulsa en la herramienta Vista de Dibujo. Por defecto, se ubicará una vista en planta a 1:1 (escala real) en la parte superior izquierda de la página. Puede que no sea visible si es demasiado pequeña o demasiado grande para la página.


</div>

Un objeto **Vista** se añade al objeto **Página** en el árbol del Proyecto. Para las siguientes vistas, un número de 3 dígitos se añadirá al nombre. Pulsa en la flecha en frente del objeto página para desplegarla y mostrar las vistas que contiene.

If only the object is selected in the Project Tree, the view is added to the first page of the project. If you have multiple pages in your project please select the object and the page it should be added to. Then click on the icon to add the view to the selected page.

### Modificar una vista existente 

Despliega el objeto Página en el árbol del Proyecto, y selecciona la vista. Sus parámetros pueden editarse en la pestaña de la vista de datos.

<img alt="" src=images/Drawing_View_Properties.png‎ ) ![Isometric view with smooth lines visibility off](images/Drawing_View_Iso.png‎  style="width:150px;"> <img alt="Isometric view with smooth lines visibility on" src=images/Drawing_View_Iso_SmoothLines.png‎‎  style="width:150px;">

-   **Etiqueta**: Cambia la etiqueta de la vista en el árbol del Proyecto. También puedes pulsar con el botón derecho sobre la vista en la vista en el árbol y seleccionar Renombrar, o seleccionar la vista y pulsar **F2**.
-   **Rotación**: gira la vista. Por ejemplo, una vista isométrica requiere una rotación de 60º (mira también el parámetro de dirección más abajo)
-   **Escala**: establece la escala de la vista.
-   **X**: establece la posición horizontal de la vista en milimetros.
-   **Y**: establece la posición horizontal de la vista en milimetros. Fíjate que la coordenada (0,0) está ubicada en la esquina superior izquierda de la página, de modo que a mayor número más abajo en la página estará la vista.
-   **Dirección**: cambia la dirección de la vista. Se establece mediante valores de XYZ que definen un vector normal a la página. La vista en planta será (0,0,1), y una isométrica (1,1,1). Los valores pueden ser negativos.
-   **Mostrar líneas ocultas**: Alterna la visibilidad de las líneas ocultas seleccionando *Verdadero* o *Falso*.
-   **Mostrar líneas de suavizado**: Alterna la visibilidad de las línea de suavizado seleccionando *Verdadero* o *Falso*. Las línea de suavizado también se denominan aristas de tangencia. Dichas aristas indican cambios entre superficies tangentes.

### Asistente de vista de dibujo 

Para generar una hoja de dibujo con vistas estándar de forma automática, utiliza la [Macro de dibujo automático](Macro_Automatic_drawing/es.md).




### Other

If you are looking for persective-orthographic toggling in 3D view check [Std PerspectiveCamera](Std_PerspectiveCamera.md) and [Std OrthographicCamera](Std_OrthographicCamera.md)


{{docnav
|[New A3 landscape drawing](Drawing_Landscape_A3.md)
|[Annotation](Drawing_Annotation.md)
|[Drawing Workbench](Drawing_Workbench.md)
|IconL=Drawing_Landscape_A3.png
|IconC=Workbench_Drawing.svg
|IconR=Drawing_Annotation.png
}}


{{Drawing Tools navi

}}



---
⏵ [documentation index](../README.md) > [Drawing](Category_Drawing.md) > Drawing View/es
