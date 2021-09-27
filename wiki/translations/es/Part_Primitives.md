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

_.

<img alt="" src=images/Part_Primitives_example.png  style="width:800px;"> 
*Las formas Primitivas que pueden ser creadas con el [Banco de trabajo Part](Part_Workbench/es.md).*

## Uso

Se puede crear una Primitiva de las siguientes maneras:

\#\* Presionando el botón **<img src="images/Part_Primitives.svg" width=24px> '''Crear Primitivas'''** en la barra de herramientas.

\#\* Seleccionando **Pieza → Crear primitivas...** desde la barra de menú.

1.  Se abre una ventana en la que se puede seleccionar el tipo de Primitiva, sus parámetros y emplazamiento, tras lo cual, pulsar sobre el botón **Crear**

La ventana de diálogo se mantiene abierta para poder seguir creando más Primitivas. Al finalizar, cerrar la ventana pulsando sobre el botón **Close**

Tras su creación, la Primitiva puede ser editada de dos maneras:

En la pestaña Modelo: {{Version/es|0.19}}

1.  Seleccionando la Primitiva y pinchando sobre ella con doble clic con el ratón, o pinchando con el botón derecho y seleccionando **Editar + Nombre de primitiva** en el menú contextual.
2.  Se abrirá la misma ventana que se utilizó para crear la Primitiva, en la que se pueden editar los parámetros deseados, pudiendo observarse los cambios en tiempo real.
3.  Aceptar los cambios pulsando el botón **OK**.

Usando el [Editor de propiedades](Property_editor/es.md):

1.  Seleccionar la Primitiva en el árbol.
2.  Editar sus propiedades en su panel de propiedades.

## Primitivas geométricas paramétricas 

Se pueden crear las siguientes Primitivas:

-   <img alt="" src=images/Part_Plane.svg  style="width:32px;"> [Plano](Part_Plane/es.md): Crea un Plano.
-   <img alt="" src=images/Tree_Part_Box_Parametric.svg  style="width:32px;"> _ .
-   <img alt="" src=images/Tree_Part_Cylinder_Parametric.svg  style="width:32px;"> _ .
-   <img alt="" src=images/Tree_Part_Cone_Parametric.svg  style="width:32px;"> _ .
-   <img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width:32px;"> _ .
-   <img alt="" src=images/Part_Ellipsoid.svg  style="width:32px;"> [Elipsoide](Part_Ellipsoid/es.md): Crea un Elipsoide.
-   <img alt="" src=images/Tree_Part_Torus_Parametric.svg  style="width:32px;"> _ .
-   <img alt="" src=images/Part_Prism.svg  style="width:32px;"> [Prisma](Part_Prism/es.md): Crea un Prisma.
-   <img alt="" src=images/Part_Wedge.svg  style="width:32px;"> [Cuña](Part_Wedge/es.md): Crea una Cuña.
-   <img alt="" src=images/Part_Helix.svg  style="width:32px;"> [Hélice](Part_Helix/es.md): Crea una Hélice.
-   <img alt="" src=images/Part_Spiral.svg  style="width:32px;"> [Espiral](Part_Spiral/es.md): Crea una Espiral.
-   <img alt="" src=images/Part_Circle.svg  style="width:32px;"> [Círculo](Part_Circle/es.md): Crea una Circunferencia (Arista circular).
-   <img alt="" src=images/Part_Ellipse.svg  style="width:32px;"> [Elipse](Part_Ellipse/es.md): Crea una Elipse (Arista elíptica).
-   <img alt="" src=images/Part_Point.svg  style="width:32px;"> [Punto](Part_Point/es.md): Crea un Punto (Vértice).
-   <img alt="" src=images/Part_Line.svg  style="width:32px;"> [Línea](Part_Line/es.md): Crea una Línea (Arista).
-   <img alt="" src=images/Part_RegularPolygon.svg  style="width:32px;"> [Polígono regular](Part_RegularPolygon/es.md): Crea un Polígono regular.

## Programación


**Ver también:**

[Part scripting](Part_scripting.md)

Comprobación de la creación de las Primitivas con una secuencia de comandos. {{Version/es|0.19}}

Esto puede ser ejecutado desde la [Consola de Python ](Python_console/es.md). 
```python
import parttests.part_test_objects as pto
pto.create_test_file("example_file")
```

Ese comando está localizado en el directorio de la instalación del programa, y puede ser examinado para ver como están construidas las Primitivas básicas. 
```python
$INSTALL_DIR/Mod/Part/parttests/part_test_objects.py
```

Se puede utilizar también como entrada de datos al programa. 
```python
freecad $INSTALL_DIR/Mod/Part/parttests/part_test_objects.py
```


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Primitives/es
