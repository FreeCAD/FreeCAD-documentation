---
 GuiCommand:
   Name: Sketcher CreateArcOfEllipse
   Name/es: Croquizador CrearArcoDeElipse
   MenuLocation: Croquis , Geometrías de Croquizador , Crear un arco de elipse
   Workbenches: Sketcher_Workbench/es
   Version: 0.15
   SeeAlso: Sketcher_CreateEllipseByCenter/es, Sketcher CompCreateArc/es
---

# Sketcher CreateArcOfEllipse/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

Esta herramienta dibuja un arco de elipse eligiendo cuatro puntos: el centro, el extremo del radio mayor, el punto inicial y el punto final. Al iniciar la herramienta, el puntero del ratón cambia a una cruz blanca con un icono de arco de elipse rojo. Además se muestran las coordenadas en tiempo real.


</div>

![](images/Sketcher_CreateArcOfEllipse_Example.png ) 
*Arc of ellipse (white) with internal geometry (dark yellow)*



## Utilización

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).


<div class="mw-translate-fuzzy">

-   Pulse el **[<img src=images/Sketcher_CreateArcOfEllipse.svg style="width:16px"> [Arco de elipse](Sketcher_CreateArcOfEllipse/es.md)**.
-   El primer clic en la vista 3D establece el centro de la elipse. El segundo clic establece el primer radio y la orientación de la elipse. El tercer clic establece el otro radio y el inicio del arco. El cuarto clic establece el final del arco.
-   Después del cuarto clic, se crea el arco de la elipse, junto con un conjunto de geometrías de construcción alineadas con él (diámetro mayor, diámetro menor, dos focos). La geometría de construcción puede ser eliminada manualmente si no se necesita, y recreada más tarde. Ver \[\[Sketcher_RestoreInternalAlignmentGeometry/es\|

Croquizador Mostrar Ocultar la geometría interna\]\].

-   Pulsar **ESC** o hacer clic con el botón derecho del ratón cancela la función.


</div>

## Notes


<div class="mw-translate-fuzzy">

## Peculiaridades

-   Los ejes mayor y menor de la elipse subyacente son estrictos y no pueden ser intercambiados por el cambio de tamaño. La elipse subyacente debe girarse para intercambiar los ejes.
-   A diferencia de la elipse, que puede ser restringida para convertirse en un círculo, el arco de la elipse no puede representar un arco de círculo.
-   Mover el arco de la elipse por el borde es lo mismo que mover el centro de la elipse.


</div>


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateArcOfEllipse/es
