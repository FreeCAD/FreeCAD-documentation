---
- GuiCommand:/es
   Name:Draft Clone
   Name/es:Borrador Clon
   MenuLocation:Modificación → Clon
   Workbenches:[Borrador](Draft_Workbench/es.md), [Arquitectura](Arch_Workbench/es.md)
   Shortcut:**C** **L**
   SeeAlso:[Borrador Escalar](Draft_Scale/es.md)
---

# Draft Clone/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

El <img alt="" src=images/Draft_Clone.svg  style="width:24px;"> comando **Borrador Clon** crea copias enlazadas, clones, de los objetos seleccionados. La forma de un clon es paramétrica, se actualizará si su objeto fuente cambia. Pero un clon tiene su propia posición, rotación y escala, y sus propias [Ver propiedades](Property_editor/es.md). Para los objetos [Arquitectura](Arch_Workbench/es.md) el comando crea un tipo especial de clon: un clon Arquitectura.


</div>


<div class="mw-translate-fuzzy">

El comando puede usarse en objetos 2D creados con el [Ambiente de Trabajo Borrador](Draft_Workbench/es.md) o [Ambiente de Trabajo Dibujante](Sketcher_Workbench/es.md), pero también en muchos objetos 3D como los creados con el [Ambiente de Trabajo Pieza](Part_Workbench/es.md), [Ambiente de Trabajo DiseñoPieza](PartDesign_Workbench/es.md) o [Ambiente de Trabajo Arquitectura](Arch_Workbench/es.md). Los clones de objetos 2D pueden utilizarse en [PartDesign Cuerpos](PartDesign_Body/es.md).


</div>

<img alt="" src=images/Draft_Clone_example.jpg  style="width:400px;"> 
*Borrador Clon junto a su objeto de origen*

## Utilización

1.  Opcionalmente selecciona uno o más objetos.
2.  Hay varias formas de invocar el comando:
    -   Pulsar el **<img src="images/Draft_Clone.svg" width=16px> [Borrador Clon](Draft_Clone/es.md)**.
    -   Seleccione la opción **Modificación → <img src="images/Draft_Clone.svg" width=16px> Clon** en el menú.
    -   Utilice el atajo de teclado: **C** y luego **L**.
3.  Si aún no ha seleccionado un objeto: seleccione un objeto en la [Vista 3D](3D_view/es.md).

## Propiedades

Ver también: [Editor de propiedades](property_editor/es.md).

Un objeto creado con el comando Clonar Borrador deriva de un [Pieza Pieza2DObjeto](Part_Part2DObject/es.md), de un objeto [Pieza Característica](Part_Feature/es.md) o, si se crea un Arch Clone, del tipo de objeto del objeto fuente. Hereda todas las propiedades de ese objeto. Un clon derivado de uno de los dos primeros objetos también tiene las siguientes propiedades adicionales:

### Datos


{{TitleProperty|Borrador}}

-    **Fusible|Bool**: especifica si las formas superpuestas en el clon se fusionan o no.

-    **Objetos|ListaEnlacesGlobal**: especifica los objetos que se clonan.

-    **Escala|Vector**: especifica los factores de escala X, Y y Z.

## Guión

Ver también: [Documentación de la API autogenerada](https://freecad.github.io/SourceDoc/) y [Fundamentos de FreeCAD Guión](FreeCAD_Scripting_Basics/es.md).

Para crear un clon utilice el método `make_clone` ({{Version/es|0.19}}) del módulo Draft. Este método sustituye al método obsoleto `clone`.


```python
cloned_object = make_clone(obj, delta=None, forcedraft=False)
```


<div class="mw-translate-fuzzy">

-    `obj`contiene los objetos a clonar. Puede ser un solo objeto o una lista de objetos.

-    `delta`es el vector de desplazamiento que se aplicará al clon.

-   Si `forcedraft` es `False` y `obj` contiene un único [Objeto Arquitectura](Arch_Workbench/es.md) se crea un Arch Clone. Establezca `forcedraft` a `True` para crear un Clon de Borrador en su lugar.

-    `cloned_object`se devuelve con el objeto clonado.


</div>

Ejemplo:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

place = App.Placement(App.Vector(1000, 0, 0), App.Rotation())
polygon1 = Draft.make_polygon(3, 750)
polygon2 = Draft.make_polygon(5, 750, placement=place)

vector = App.Vector(2600, 500, 0)
cloned_object = Draft.clone([polygon1, polygon2], delta=vector)

cloned_object.Fuse = True

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Clone/es
