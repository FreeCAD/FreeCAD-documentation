---
- GuiCommand:
   Name:Draft PointArray
   Name/es:Borrador ArregloPunto
   MenuLocation:Modificación - Herramientas de  Arreglo - Arreglo Punto
   Workbenches:[Borrador](Draft_Workbench/es.md), [Arquitectura](Arch_Workbench/es.md)
   Version:0.18
   SeeAlso:[Borrador OrthoArray](Draft_OrthoArray/es.md), [Borrador ArregloPolar](Draft_PolarArray/es.md), 
[Borrador ArregloCircular](Draft_CircularArray/es.md), [Borrador ArregloRuta](Draft_PathArray/es.md), [Borrador ArregloEnlaceRuta](Draft_PathLinkArray/es.md), [Borrador ArregloEnlacePunto](Draft_PointLinkArray/es.md)
---

# Draft PointArray/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

El comando <img alt="" src=images/Draft_PointArray.svg  style="width:24px;"> El comando **Borrador ArregloPuntos** crea una arreglo regular a partir de un objeto seleccionado colocando copias en los puntos de un [compuesto puntos](#Compuesto_puntos.md). Utilice el comando [Borrador ArregloEnlacePunto](Draft_PointLinkArray/es.md) para crear un arreglo [Enlace](App_Link/es.md) más eficiente. Excepto por el tipo de arreglo que se crea, arreglo de enlace o matriz normal, el comando [Borrador ArregloEnlacePunto](Draft_PointLinkArray/es.md) es idéntico a este comando.


</div>


<div class="mw-translate-fuzzy">

Ambos comandos pueden utilizarse en objetos 2D

creados con el [Ambiente de Trabajo Borrador](Draft_Workbench/es.md) o [Ambiente de Trabajo Dibujo](Sketcher_Workbench/es.md), pero también en muchos objetos 3D como los creados con el [Ambiente de Trabajo Pieza](Part_Workbench/es.md), [Ambiente de Trabajo DiseñoPieza](PartDesign_Workbench/es.md) o [Ambiente de Trabajo Arquitectura](Arch_Workbench/es.md).


</div>

The point object can be any object with a shape and vertices (including a [Std Part](Std_Part.md) containing one or more of such objects), as well as a [mesh](Mesh_Workbench.md) and a [point cloud](Points_Workbench.md). Duplicate points in the point object are filtered out. <small>(v0.21)</small> 

In {{VersionMinus|0.20}} only three point object types are supported see [Point object version 0.20 and below](#Point_object_version_0.20_and_below.md).

<img alt="" src=images/Draft_PointArray_Example.png  style="width:400px;"> 
*Borrador ArregloPunto*



## Utilización

1.  Seleccione el objeto que desea formar un array.
2.  Añade el objeto [punto compuesto](#Punto_compuesto.md) a la selección.
3.  Hay varias formas de invocar el comando:
    -   Pulsar el **<img src="images/Draft_PointArray.svg" width=16px> [Borrador ArregloPunto](Draft_PointArray/es.md)**.
    -   Seleccione la opción **Modificación → Herramientas de arreglo →<img src="images/Draft_PointArray.svg" width=16px> Arreglo de puntos** en el menú.
4.  Se crea el arreglo.
5.  Opcionalmente cambia las [propiedades](#Propiedades.md) del arreglo en el [Editor de propiedades](property_editor/es.md).

## Point object version 0.20 and below 


<div class="mw-translate-fuzzy">

Un compuesto de puntos es un objeto que contiene uno o más puntos. Estos son los compuestos de puntos soportados y cómo se pueden crear:

-   [Compuesta Pieza](Part_Compound.md): Cree uno o más [Borrador Puntos](Draft_Point/es.md) o [Pieza Puntos](Part_Point/es.md), selecciónelos e invoque el comando [Compuesta Pieza](Part_Compound/es.md).
-   Bloque de borrador: Crea uno o más [Borrador Puntos](Draft_Point/es.md) o [Pieza Puntos](Part_Point/es.md), selecciónalos e invoca el comando [Borrador Actualización](Draft_Upgrade/es.md).
-   [Croquizador Croquis](Sketcher_NewSketch/es.md): Crea un [Croquis](Sketcher_NewSketch/es.md) y añade uno o más [Croquizador Puntos](Sketcher_CreatePoint/es.md) al croquis.


</div>



## Propiedades

Ver también: [Editor de propiedades](property_editor/es.md).

Un objeto Borrador ArregloPunto deriva de un objeto [Pieza Función](Part_Feature/es.md) y hereda todas sus propiedades (con la excepción de algunas propiedades de la Vista que no son heredadas por los arreglos enlace). Las siguientes propiedades son adicionales a menos que se indique lo contrario:



### Datos


{{TitleProperty|Link}}

The properties in this group are only available for Link arrays. See [Std LinkMake](Std_LinkMake#Properties.md) for more information.

-    **Scale|Float**
    

-    **Scale Vector|Vector|Hidden**
    

-    **Scale List|VectorList**
    

-    **Visibility List|BoolList|Hidden**
    

-    **Placement List|PlacementList|Hidden**
    

-    **Element List|LinkList|Hidden**
    

-    **_ Link Touched|Bool|Hidden**
    

-    **_ Child Cache|LinkList|Hidden**
    

-    **Colored Elements|LinkSubHidden|Hidden**
    

-    **Link Transform|Bool**
    


{{TitleProperty|Objetos}}

-    **Base|Link**: specifies the object to duplicate in the array.

-    **Count|Integer**: (read-only) specifies the number of elements in the array. This number is determined by the number of points in the **Point Object**.

-    **Expand Array|Bool**: specifies whether to expand the array in the [Tree view](Tree_view.md) to enable the selection of its individual elements. Only available for Link arrays.

-    **Extra Placement|Placement**: : specifies an additional [placement](Placement.md), translation and rotation, for each element in the array.

-    **Point Object|Link**: specifies the compound object whose points are used to position the elements in the array. The object must have a **Links**, **Components** or **Geometry** property, and contain at least one element with **X**, **Y**, and **Z** properties.



### Vista


{{TitleProperty|Enlace}}

The properties in this group, with the exception of the inherited property, are only available for Link arrays. See [Std LinkMake](Std_LinkMake#Properties.md) for more information.

-    **Draw Style|Enumeration**
    

-    **Line Width|FloatConstraint**
    

-    **Override Material|Bool**
    

-    **Point Size|FloatConstraint**
    

-    **Selectable|Bool**: this is an inherited property that appears in the Selection group for other arrays

-    **Shape Material|Material**
    


{{TitleProperty|Base}}

The properties in this group, with the exception of the inherited property, are only available for Link arrays. See [Std LinkMake](Std_LinkMake#Properties.md) for more information.

-    **Child View Provider|PersistentObject|Hidden**
    

-    **Material List|MaterialList|Hidden**
    

-    **Override Color List|ColorList|Hidden**
    

-    **Override Material List|BoolList|Hidden**
    

-    **Proxy|PythonObject|Hidden**: this is an inherited property.


{{TitleProperty|Display Options}}

The properties in this group are inherited properties. See [Part Feature](Part_Feature#Properties.md) for more information.

-    **Bounding Box|Bool**: this property is not inherited by Link arrays.

-    **Display Mode|Enumeration**: for Link arrays it can be {{value|Link}} or {{value|ChildView}}. For other arrays it can be: {{value|Flat Lines}}, {{value|Shaded}}, {{value|Wireframe}} or {{value|Points}}

-    **Show In Tree|Bool**
    

-    **Visibility|Bool**
    


{{TitleProperty|Borrador}}

-    **Pattern|Enumeration**: not used.

-    **Pattern Size|Float**: not used.


{{TitleProperty|Object style}}

The properties in this group are not inherited by Link arrays.



## Guión

Ver también: [Documentación de la API autogenerada](https://freecad.github.io/SourceDoc/) y [Fundamentos de FreeCAD Guión](FreeCAD_Scripting_Basics/es.md).

To create a point array use the `make_point_array` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makePointArray` method.


```python
point_array = make_point_array(base_object, point_object, extra=None, use_link=True)
```

-    `base_object`is the object to be arrayed. It can also be the `Label` (string) of an object in the current document.

-    `point_object`is the object containing the points. It can also be the `Label` (string) of an object in the current document. It should have a `Geometry`, `Links`, or `Components` property containing points.

-    `extra`is an `App.Placement`, an `App.Vector` or an `App.Rotation` that displaces each element.

-   If `use_link` is `True` the created elements are [App Links](App_Link.md) instead of regular copies.

Ejemplo:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon = Draft.make_polygon(3, radius=500.0)

p1 = Draft.make_point(App.Vector(1500, 0, 0))
p2 = Draft.make_point(App.Vector(2500, 0, 0))
p3 = Draft.make_point(App.Vector(2000, 1000, 0))

compound = doc.addObject("Part::Compound", "Compound")
compound.Links = [p1, p2, p3]

point_array = Draft.make_point_array(polygon, compound)
doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft PointArray/es
