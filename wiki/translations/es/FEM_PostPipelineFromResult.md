---
- GuiCommand:   Name:FEM PostPipelineFromResult   MenuLocation: Results → post pipeline from result   |Workbenches:[Shortcut:   SeeAlso:[[FEM_tutorial|FEM tutorial](FEM_Workbench___FEM]].md)---


</div>

**\* You need a valid result object in the **<img src="images/FEM_Analysis.svg" width=24px> [Analysis container](FEM_Analysis.md)
**, such as **CalculiX static results**.**

## Description


<div class="mw-translate-fuzzy">

## Descripción

Pipeline es un objeto de resultado, que crea una nueva representación gráfica de los resultados del análisis FEM en la parte analizada. Añade escala de colores y más opciones de visualización.


</div>

## Usage


<div class="mw-translate-fuzzy">

## Cómo usar 

-   Necesita un objeto de resultado válido en {{KEY | <img src="images/_FEM_Analysis.png_" width= 24px> [Analysis container](FEM_Analysis/es.md)}}, como {{KEY | CalculiX_static_results}}.
-   Seleccione el objeto de resultado
-   Haga clic en el botón <img alt="" src=images/_FEM_PostPipelineFromResult.png  style="width:24px;">, o haga clic en el menú **Results** y el elemento **Post Pipeline from results**. Se agregará un nuevo objeto llamado \"Pipeline\" a su documento; note si aparecerá fuera del contenedor de análisis.
-   Haga doble clic en el nuevo objeto Pipeline en el árbol Modelo y seleccione el tipo de propiedades para mostrar. Las configuraciones típicas son: Modo: Seleccione **Superficie**, Campo: Es decir. **Von Mises stress** ![](images/_Pipeline.PNG )
    -   Modo: Cómo dibujar los resultados.
    -   Campo: Qué propiedad del resultado dibujar.
    -   Vector: Si una propiedad es un vector, puede restringir los datos a un eje (X, Y, Z) o seleccionar Magnitud para usar el valor del vector.
-   Si no ve ningún modelo en el área gráfica, vaya a **Edit** → **Preferences**, seleccione la categoría **Display** y marque una casilla **Enable backlight color} }
    * Si hace doble clic en la escala, puede modificar las propiedades de visualización.
    [[File:SIMTUT 05.PNG]]
    ** Degradado: puede seleccionar el orden inverso del degradado de color predeterminado o Negro-Blanco o Blanco-Negro.
    ** Rango de parámetros: los valores mínimo y máximo se completan automáticamente, cuando selecciona una propiedad para evaluar en el objeto {{KEY|Pipeline**; Puedes modificarlos, pero asegúrate de saber lo que estás haciendo. También puede modificar el número de etiquetas mostradas y el número de decimales que se mostrarán.
    </div>

    ==Limitaciones==

    Una vez más, tenga en cuenta que la representación de la tubería de los resultados (llamados VTK) en la parte mostrada es diferente de los resultados del gradiente de color que son visibles cuando termina la solución. Los valores en la escala de degradado no se pueden aplicar al objeto de resultado de la solución.


    

    {{FEM Tools navi}}


 
