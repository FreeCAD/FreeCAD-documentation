---
- GuiCommand:/es
   Name:Sketcher CreateLine
   Name/es:Croquizador CrearLínea
   MenuLocation:Croquis → Geometría de croquizador → Crear línea
   Workbenches:[Croquizador](Sketcher_Workbench/es.md)
   Shortcut:L
   SeeAlso:[Croquizador Polilínea](Sketcher_CreatePolyline/es.md)
---

# Sketcher CreateLine/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

Esta herramienta dibuja una línea indicando dos puntos en la vista 3D. Cuando se inicia la herramienta, el puntero del ratón cambia a una cruz blanca con un icono de línea rojo. Además se muestran las coordenadas en tiempo real.


</div>

![](images/Sketcher_LineExample1.png‎ )


<div class="mw-translate-fuzzy">

El objeto línea creado comienza y termina en los puntos dados, pero la línea es infinita respecto a las restricciones [Tangente](Sketcher_ConstrainTangent/es.md), [PuntoEnObjeto](Sketcher_ConstrainPointOnObject/es.md) y [ÁnguloInterno](Sketcher_ConstrainAngle/es.md). Esto significa, por ejemplo, que un punto con la restricción [PuntoEnObjeto](Sketcher_ConstrainPointOnObject/es.md) puede no estar situado entre los dos puntos dados, sino que puede estar fuera de los dos puntos en la extensión de la línea dibujada.


</div>



## Utilización


<div class="mw-translate-fuzzy">

-   Elegir puntos en un área vacía de la vista 3d, o en un objeto existente (las restricciones automáticas deben estar activas en TaskView).
-   Pulsando **Esc** o haciendo clic con el botón derecho del ratón se cancela la función.


</div>





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateLine/es
