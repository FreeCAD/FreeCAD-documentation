---
- GuiCommand:/es
   Name:Ship Outline
   Name/es:Contorno del buque
   Icon:Ship_OutlineDraw.svg
   MenuLocation:Diseño del buque → Dibujo del contorno
   Workbenches:[Barco](Ship_Workbench/es.md)
   Shortcut:
   SeeAlso:
---

# Ship Outline/es


**Warning. This tool is outdated and will be removed from the module. You can instead consider the [Cross-sections](Part_CrossSections.md) tool to compute the intersections, and the [Drawing workbench](Drawing_Workbench.md) to plot them**

## Descripción

Dibuja el contorno del casco del barco

## Dibujo de líneas 

El barco proporciona una herramienta que facilita la obtención de un plano de líneas a partir del dibujo de líneas del barco

![Herramienta de dibujo de líneas](images/Ship_OutlineDraw.svg )


<center>

Icono de la herramienta de dibujo de líneas


</center>

El dibujo de líneas es un conjunto de líneas de cortes de sección en los 3 ejes, que finalmente mostrarán la geometría del casco en un Plano de Líneas. Necesitamos proporcionar las líneas para las 3 siguientes vistas:

-   Plano del cuerpo (usando los cortes transversales)
-   Plano de la carena (usando los cortes longitudinales)
-   Plano de media manga (usando los cortes de líneas de agua)

### Cortes transversales 

Normalmente hay que realizar 21 secciones transversales equidistantes entre perpendiculares. para ello FreeCAD proporciona una herramienta automática para hacerlo, simplemente selecciona el tipo de secciones **Transversales**, ve a la casilla **Auto crear** y pon **21** secciones, luego pulsa **Crear secciones**.

![Previsualización de las secciones transversales del dibujo de contorno](images/S60OutlineTransversal.png )


<center>

Previsualización de las secciones transversales de Outline


</center>

La tabla de secciones se llena, y se muestra la vista previa de las secciones llamada **DibujoContorno**. Normalmente se añaden más secciones en la proa y en la popa, donde se registran curvaturas más complejas, para hacerlo vaya al final de la tabla, y haga *doble clic* en el elemento vacío para editarlo, pulsando intro para confirmar. Agregue las siguientes secciones:

-   X~22~ = -12.1125 m
-   X~23~ = 12.1125 m

Dependiendo de la complejidad de la geometría del casco, la vista previa de las secciones puede llevar algún tiempo. Para eliminar una sección, basta con rellenarla con un texto vacío y pulsar Intro.

### Cortes longitudinales 

Hay que añadir dos cortes longitudinales, por lo que hay que seleccionar el tipo de secciones **Longitudinales**, ir a la casilla **Creación automática**\' y poner **2** secciones, luego pulsar **Crear secciones**. Tabla de secciones se llena, y la vista previa de las secciones actualizadas.

### Líneas de agua 

6 Líneas de agua entre la línea base y el proyecto de diseño debe ser añadido, así que seleccione **Líneas de agua** tipo de secciones, vaya a **Auto crear**\' caja y establecer **5**\' (Z = 0 m no se considerará, añadir manualmente si lo necesita) secciones, a continuación, pulse **Crear secciones**. La tabla de secciones se llena, y la vista previa de las secciones se actualiza.

Several additional waterlines must be added:

-   Z~6~ = 1.2 m
-   Z~7~ = 1.4 m
-   Z~8~ = 1.6 m
-   Z~9~ = 1.8 m
-   Z~10~ = 2.0 m

### Perform plot 

Select **1:100** scale and press **Accept** to let the tool to generate the 3D sections in a new object.

![Resultant sections.](images/FreeCAD-Ship-S60Outline3DSections.png )


<center>

Resultant sections.


</center>

In order to plot these sections you can use the [Drawing workbench](Drawing_Workbench.md):

![Outline draw plot.](images/FreeCAD-Ship-S60OutlinePlot.png )


<center>

Outline draw plot.


</center>

## Tutoriales

-   [Tutorial de FreeCAD-Nave s60 ](FreeCAD-Ship_s60_tutorial/es.md)
-   [Tutorial de FreeCAD-Nave s60 (II)](FreeCAD-Ship_s60_tutorial_(II)/es.md)





{{Ship_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Ship Outline/es
