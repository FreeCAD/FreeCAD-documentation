---
- GuiCommand:/es
   Name:Sketcher CreateEllipseByCenter
   Name/es:Croquizador CrearElipsePorCentro
   MenuLocation:Croquis → Geometrías del Croquizador → Crear elipse por centro
   Workbenches:[Croquizador](Sketcher_Workbench/es.md)
   Version:0.15
   SeeAlso:[Croquizador  Elipse de 3 puntos](Sketcher_CreateEllipseBy3Points/es.md), [Croquizador Círculo](Sketcher_CreateCircle/es.md), [Croquizador Arco de Elipse](Sketcher_CreateArcOfEllipse/es.md)
---

# Sketcher CreateEllipseByCenter/es

## Descripción

Esta herramienta dibuja una elipse eligiendo tres puntos: el centro, el extremo del radio mayor y el radio menor. Al iniciar la herramienta, el puntero del ratón cambia a una cruz blanca con un icono de elipse rojo. Además se muestran las coordenadas en tiempo real.

<img alt="" src=images/Sketcher_EllipseExample1.png‎  style="width:500px;">



*La secuencia de clics se indica con flechas amarillas con números. C es el centro, a - diámetro mayor, b - diámetro menor, F1, F2 son focos.*

## Utilización

-   Invoca el comando haciendo clic en un botón de la barra de herramientas, eligiendo el elemento del menú, o utilizando el atajo de teclado (necesita ser asignado primero en [Personalización de la interfaz](Interface_Customization/es.md)).
-   El primer clic en la vista 3D establece el centro de la elipse. El segundo clic establece el primer radio y la orientación de la elipse. El tercer clic establece el otro radio (la distancia desde la línea definida por los dos primeros clics es el segundo radio).
-   Después del tercer clic, se crea la elipse, junto con un conjunto de geometría de construcción alineada con ella (diámetro mayor, diámetro menor, dos focos). La geometría de construcción puede ser eliminada manualmente si no se necesita, y recreada más tarde. Ver [Restricción de alineación interna](Sketcher_ConstrainInternalAlignment/es.md) y [Croquizador Mostrar Ocultar la geometría interna](Sketcher_RestoreInternalAlignmentGeometry/es.md).
-   Pulsar **ESC** o hacer clic con el botón derecho del ratón cancela la función.

## Peculiaridades

-   Los ejes mayor y menor de las elipses son estrictos y no se pueden intercambiar cambiando el tamaño de la elipse. Esto es una consecuencia de la parametrización del solver utilizada (centro (x,y), foco1 (x,y) y longitud de radio menor (b)) y del mismo comportamiento estricto de OpenCascade. La elipse debe ser girada para intercambiar los ejes.
-   La elipse puede funcionar como un círculo cuando se eliminan sus líneas de diámetro mayor y menor, y se restringe uno de los focos para que coincida con el centro. Pero la restricción del radio no funcionará en dicho círculo.
-   Mover la elipse por el borde es lo mismo que mover el centro de la elipse.





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateEllipseByCenter/es
