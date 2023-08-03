---
 GuiCommand:
Name=Sketcher CreateEllipseBy3Points
Name/es=Croquizador CrearElipsePor3Puntos
   MenuLocation: Croquis , Geometrías del Croquizador , Crear elipse por 3 puntos
   Workbenches: Sketcher_Workbench/es
   Version: 0.15
   SeeAlso: Sketcher_CreateEllipseByCenter/es, Sketcher_CreateCircle/es, Sketcher_CreateArcOfEllipse/es
---

# Sketcher CreateEllipseBy3Points/es


</div>



## Descripción

Esta herramienta dibuja una elipse eligiendo tres puntos : (1) la periapsis (primer cruce del diámetro mayor con la elipse), (2) la apoapsis (segundo cruce del diámetro mayor con la elipse), (3) un punto en un lado del diámetro mayor (a) que define el radio menor (b). (c) es el centro resultante y (f) son los puntos focales.

Al iniciar la herramienta, el puntero del ratón cambia a una cruz blanca con un icono de elipse roja.

![](images/Ellipse_3Point.png‎ )


<div class="mw-translate-fuzzy">



*La secuencia de clics se indica con flechas amarillas con números. 1 es la periapsis, 2 es la apoapsis, 3 es el punto de definición del diámetro menor, las líneas verdes son los diámetros mayor y menor. Las líneas azules son líneas de construcción aleatorias sólo para fines ilustrativos.*


</div>



## Utilización


<div class="mw-translate-fuzzy">

-   Pulse el **[<img src=images/Sketcher_CreateEllipseBy3Points.svg style="width:16px"> [Ellipse por 3 puntos](Sketcher_CreateEllipseBy3Points/es.md)**.
-   El primer clic en la vista 3D establece un punto que define el cruce del diámetro mayor con la elipse (periapsis). El segundo clic en la vista 3D establece un punto que define el cruce del diámetro mayor con la elipse opuesto al punto central (apoapsis). El tercer clic establece un punto en la elipse que define el radio menor.


</div>

-   Después del tercer clic, se crea la elipse, junto con un conjunto de geometría de construcción alineada con ella (diámetro mayor, diámetro menor, dos focos). La geometría de construcción puede eliminarse manualmente si no se necesita, y volver a crearse más tarde. Ver [Croquizador Mostrar Ocultar Geometría Interna](Sketcher_RestoreInternalAlignmentGeometry/es.md).
-   Pulsar **ESC** o hacer clic con el botón derecho del ratón cancela la función.

## Peculiarities


<div class="mw-translate-fuzzy">

## Peculiaridades

-   Los ejes mayor y menor de las elipses son estrictos y no se pueden intercambiar cambiando el tamaño de la elipse. Esto es una consecuencia de la parametrización del solver utilizada (centro (x,y), foco1 (x,y) y longitud de radio menor (b)) y del mismo comportamiento estricto de OpenCascade. La elipse debe ser girada para intercambiar los ejes.
-   La elipse puede funcionar como un círculo cuando se eliminan sus líneas de diámetro mayor y menor, y se restringe uno de los focos para que coincida con el centro. Pero la restricción del radio no funcionará en dicho círculo.
-   Mover la elipse por el borde es lo mismo que mover el centro de la elipse.


</div>


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateEllipseBy3Points/es
