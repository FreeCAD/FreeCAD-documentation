---
 GuiCommand:
   Name: Sketcher CreateEllipseByCenter
   Name/es: Croquizador CrearElipsePorCentro
   MenuLocation: Croquis , Geometrías del Croquizador , Crear elipse por centro
   Workbenches: Sketcher_Workbench/es
   Version: 0.15
   SeeAlso: Sketcher_CreateEllipseBy3Points/es, Sketcher_CreateCircle/es, Sketcher_CreateArcOfEllipse/es
---

# Sketcher CreateEllipseByCenter/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

Esta herramienta dibuja una elipse eligiendo tres puntos: el centro, el extremo del radio mayor y el radio menor. Al iniciar la herramienta, el puntero del ratón cambia a una cruz blanca con un icono de elipse rojo. Además se muestran las coordenadas en tiempo real.


</div>

![](images/Sketcher_CreateEllipseByCenter_Example.png ) 
*Ellipse (white) with internal geometry (dark yellow)*



## Utilización

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

Pos-OVP = Positional [On-View-Parameters](Sketcher_Preferences#General.md). <small>(v1.0)</small> 
Dim-OVP = Dimensional On-View-Parameters. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   Invoca el comando haciendo clic en un botón de la barra de herramientas, eligiendo el elemento del menú, o utilizando el atajo de teclado (necesita ser asignado primero en [Personalización de la interfaz](Interface_Customization/es.md)).
-   El primer clic en la vista 3D establece el centro de la elipse. El segundo clic establece el primer radio y la orientación de la elipse. El tercer clic establece el otro radio (la distancia desde la línea definida por los dos primeros clics es el segundo radio).
-   Después del tercer clic, se crea la elipse, junto con un conjunto de geometría de construcción alineada con ella (diámetro mayor, diámetro menor, dos focos). La geometría de construcción puede ser eliminada manualmente si no se necesita, y recreada más tarde. Ver [Croquizador Mostrar Ocultar la geometría interna](Sketcher_RestoreInternalAlignmentGeometry/es.md).
-   Pulsar **ESC** o hacer clic con el botón derecho del ratón cancela la función.


</div>

## Notes


<div class="mw-translate-fuzzy">

-   Los ejes mayor y menor de las elipses son estrictos y no se pueden intercambiar cambiando el tamaño de la elipse. Esto es una consecuencia de la parametrización del solver utilizada (centro (x,y), foco1 (x,y) y longitud de radio menor (b)) y del mismo comportamiento estricto de OpenCascade. La elipse debe ser girada para intercambiar los ejes.
-   La elipse puede funcionar como un círculo cuando se eliminan sus líneas de diámetro mayor y menor, y se restringe uno de los focos para que coincida con el centro. Pero la restricción del radio no funcionará en dicho círculo.
-   Mover la elipse por el borde es lo mismo que mover el centro de la elipse.


</div>


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateEllipseByCenter/es
