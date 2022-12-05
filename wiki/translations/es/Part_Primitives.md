---
- GuiCommand:/es
   Name:Part Primitives
   Name/es:Part Crear Primitivas
   MenuLocation:Pieza → Crear primitivas...
   |Workbenches:[Part](Part_Workbench/es.md)
   SeeAlso:[Part Shapebuilder](Part_Builder.md)
---

# Part Primitives/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

[Part Primitivas](Part_Primitives/es.md) Abre una caja de diálogo para crear cualquiera de las primitivas geométricas paramétricas definidas en el <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Banco de trabajo Part](Part_Workbench/es.md).


</div>

<img alt="" src=images/Part_Primitives_example.png  style="width:600px;">


<div class="mw-translate-fuzzy">



*Las formas Primitivas que pueden ser creadas con el [Banco de trabajo Part](Part_Workbench/es.md).*


</div>

## Uso

### Create


<div class="mw-translate-fuzzy">

Se puede crear una Primitiva de las siguientes maneras:

#\* Presionando el botón **<img src="images/Part_Primitives.svg" width=24px> '''Crear Primitivas'''** en la barra de herramientas.

#\* Seleccionando **Pieza → Crear primitivas...** desde la barra de menú.

1.  Se abre una ventana en la que se puede seleccionar el tipo de Primitiva, sus parámetros y emplazamiento, tras lo cual, pulsar sobre el botón **Crear**

La ventana de diálogo se mantiene abierta para poder seguir creando más Primitivas. Al finalizar, cerrar la ventana pulsando sobre el botón **Close**


</div>

### Edit


<div class="mw-translate-fuzzy">

En la pestaña Modelo: {{Version/es|0.19}}

1.  Seleccionando la Primitiva y pinchando sobre ella con doble clic con el ratón, o pinchando con el botón derecho y seleccionando **Editar + Nombre de primitiva** en el menú contextual.
2.  Se abrirá la misma ventana que se utilizó para crear la Primitiva, en la que se pueden editar los parámetros deseados, pudiendo observarse los cambios en tiempo real.
3.  Aceptar los cambios pulsando el botón **OK**.


</div>

The properties of a Part Primitive can also be changed in the [Property editor](Property_editor.md), and its **Placement** can also be changed with the <img alt="" src=images/Std_TransformManip.svg  style="width:16px;"> [Std TransformManip](Std_TransformManip.md) command.

## Primitivas geométricas paramétricas 


<div class="mw-translate-fuzzy">

Se pueden crear las siguientes Primitivas:

-   <img alt="" src=images/Part_Plane.svg  style="width:32px;"> [Plano](Part_Plane/es.md): Crea un Plano.
-   <img alt="" src=images/Tree_Part_Box_Parametric.svg  style="width:32px;"> [Caja](Part_Box/es.md): Crea una Caja. Este objeto puede ser creado también con la herramienta <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Cubo](Part_Box/es.md) .
-   <img alt="" src=images/Tree_Part_Cylinder_Parametric.svg  style="width:32px;"> [Cilindro](Part_Cylinder/es.md): Este objeto puede ser creado también con la herramienta <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Cilindro](Part_Cylinder/es.md) .
-   <img alt="" src=images/Tree_Part_Cone_Parametric.svg  style="width:32px;"> [Cono](Part_Cone/es.md): Crea un Cono. Este objeto puede ser creado también con la herramienta <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Cono](Part_Cone/es.md) .
-   <img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width:32px;"> [Esfera](Part_Sphere/es.md): Crea una Esfera. Este objeto puede ser creado también con la herramienta <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Esfera](Part_Sphere/es.md) .
-   <img alt="" src=images/Part_Ellipsoid.svg  style="width:32px;"> [Elipsoide](Part_Ellipsoid/es.md): Crea un Elipsoide.
-   <img alt="" src=images/Tree_Part_Torus_Parametric.svg  style="width:32px;"> [Toro](Part_Torus/es.md): Crea un Toro. Este objeto puede ser creado también con la herramienta <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Toro](Part_Torus/es.md) .
-   <img alt="" src=images/Part_Prism.svg  style="width:32px;"> [Prisma](Part_Prism/es.md): Crea un Prisma.
-   <img alt="" src=images/Part_Wedge.svg  style="width:32px;"> [Cuña](Part_Wedge/es.md): Crea una Cuña.
-   <img alt="" src=images/Part_Helix.svg  style="width:32px;"> [Hélice](Part_Helix/es.md): Crea una Hélice.
-   <img alt="" src=images/Part_Spiral.svg  style="width:32px;"> [Espiral](Part_Spiral/es.md): Crea una Espiral.
-   <img alt="" src=images/Part_Circle.svg  style="width:32px;"> [Círculo](Part_Circle/es.md): Crea una Circunferencia (Arista circular).
-   <img alt="" src=images/Part_Ellipse.svg  style="width:32px;"> [Elipse](Part_Ellipse/es.md): Crea una Elipse (Arista elíptica).
-   <img alt="" src=images/Part_Point.svg  style="width:32px;"> [Punto](Part_Point/es.md): Crea un Punto (Vértice).
-   <img alt="" src=images/Part_Line.svg  style="width:32px;"> [Línea](Part_Line/es.md): Crea una Línea (Arista).
-   <img alt="" src=images/Part_RegularPolygon.svg  style="width:32px;"> [Polígono regular](Part_RegularPolygon/es.md): Crea un Polígono regular.


</div>

## Notes

-   The Part Primitives command cannot create a <img alt="" src=images/Part_Tube.svg  style="width:16px;"> [Part Tube](Part_Tube.md).

## Programación

See also: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/), [Part scripting](Part_scripting.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


<div class="mw-translate-fuzzy">

Comprobación de la creación de las Primitivas con una secuencia de comandos. {{Version/es|0.19}}


</div>


```python
import parttests.part_test_objects as pto
pto.create_test_file("example_file")
```


<div class="mw-translate-fuzzy">

Ese comando está localizado en el directorio de la instalación del programa, y puede ser examinado para ver como están construidas las Primitivas básicas.


</div>


```python
$INSTALL_DIR/Mod/Part/parttests/part_test_objects.py
```


<div class="mw-translate-fuzzy">

Se puede utilizar también como entrada de datos al programa.


</div>


```python
freecad $INSTALL_DIR/Mod/Part/parttests/part_test_objects.py
```


<div class="mw-translate-fuzzy">





</div>


{{Part_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Primitives/es
