---
- GuiCommand:/es
   Name:Part Plane
   Name/es:Part Plano
   MenuLocation:Pieza → Crear primitivas... →Plano
   |Workbenches:[Part](Part_Workbench/es.md)
   SeeAlso:[Part Primitivas](Part_Primitives/es.md)
---

# Part Plane/es


</div>

## Description


<div class="mw-translate-fuzzy">

## Descripción

Crea un Plano paramétrico simple de 10 x 10 mm, con los parámetros de posición, longitud y anchura. Por defecto, el Plano es colocado en el origen (0,0,0).


</div>

![](images/PartPlane.png )

## Uso

El Plano estándar es creado con su esquina inferior izquierda en el punto de origen `0,0,0`. Para cambiar estos parámetros, abrir la sección de Ubicación e introducir los valores deseados en sus respectivos campos de entrada, o pinchar en la [vista 3D](3D_view/es.md) y seleccionar un punto, los puntos de coordenadas son tomados de los campos. En el menú de Dirección se puede también definir un vector estándar (X, Y o Z) normal al plano, o pinchar Definido por el usuario\... para abrir la caja de diálogo que permite seleccionar un vector diferente (por ejemplo, la dirección 1.0 , -1 crea un plano inclinado 45° con respecto a X y Z).


<div class="mw-translate-fuzzy">

Las propiedades pueden ser cambiadas posteriormente en la pestaña **Vista combinada → Datos**, tras seleccionar el objeto.


</div>

## Properties

### Data


{{TitleProperty|Base}}

-    **Label**: String name of the object, defaults to \'Plane\'. User may rename it.

-    **Placement**: Placement of feature is defined by below angle, axis and position.

-    **Angle**: Angle of rotation relative to the below axis.

-    **Axis**: Defines the axis of rotation plane: X, Y, or Z. Defaults to Z axis, Z = 1

-    **Position**: Position X, Y, Z, relative to the origin 0, 0, 0.


{{TitleProperty|Plane}}

-    **Length**: Length is the dimension along the X axis The default value is 10 mm

-    **Width**: Width is the size of the Y-axis The default value is 10 mm

### View

You have the standard properties view.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Plane/es
