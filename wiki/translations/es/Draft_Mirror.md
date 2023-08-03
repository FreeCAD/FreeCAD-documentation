---
 GuiCommand:
   Name: Draft Mirror
   Name/es: Draft Mirror
   MenuLocation: Draft , Mirror
   Workbenches: Draft_Workbench/es, Arch_Workbench/es
   SeeAlso: Draft Scale/es
---

# Draft Mirror/es


</div>

## Description


<div class="mw-translate-fuzzy">

## Descripción

Esta herramienta produce una copia duplicada de un objeto seleccionado, utilizando un objeto [Part Mirror](Part_Mirror.md). La copia está vinculada de forma paramétrica al objeto original: si el objeto original cambia, la copia duplicada también cambia, pero se mantiene reflejada.


</div>

The command can be used on 2D objects created with the [Draft Workbench](Draft_Workbench.md) or [Sketcher Workbench](Sketcher_Workbench.md), but also on many 3D objects such as those created with the [Part Workbench](Part_Workbench.md), [PartDesign Workbench](PartDesign_Workbench.md) or [Arch Workbench](Arch_Workbench.md).

<img alt="" src=images/Draft_Mirror_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_Mirror_example.jpg  style="width:400px;">


</div>

## Usage

See also: [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## Comment utiliser 

1.  Sélectionnez les objets que vous souhaitez mettre en miroir
2.  Appuyez sur le bouton {{KEY | <img src="images/_Draft_Mirror.png_" width= 16px> [[Draft Mirror]]}}.
3.  Cliquez sur le premier point de la ligne miroir sur la vue 3D ou tapez une coordonnée
4.  Cliquez sur l\'autre point de la ligne miroir de la vue 3D ou tapez une coordonnée


</div>

## Options

The single character keyboard shortcuts mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).


<div class="mw-translate-fuzzy">

## Opciones

-   Después de la creación del espejo, su enlace con el objeto original se puede eliminar con la herramienta [ Part Simple Copy](Part_SimpleCopy.md).
-   El espejo de un objeto Draft también se puede convertir en un Draft Wire, usando [Draft Downgrade](Draft_Downgrade.md) luego [Draft Upgrade](Draft_Upgrade.md).


</div>

## Notes

-   Mirrored copies of [Draft Lines](Draft_Line.md), [Draft Wires](Draft_Wire.md), [Draft Arcs](Draft_Arc.md) and [Draft Circles](Draft_Circle.md) can be turned into independent editable Draft objects by using [Draft Downgrade](Draft_Downgrade.md) and then [Draft Upgrade](Draft_Upgrade.md).
-   The [Part SimpleCopy](Part_SimpleCopy.md) command can be used to create a copy of a mirrored object that is not linked to its source object.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.

## Properties

See also: [Property editor](property_editor.md).

A [Part Mirror](Part_Mirror.md) object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Base}}

-    **Source|Link**: specifies the object that is mirrored.


{{TitleProperty|Plane}}


<div class="mw-translate-fuzzy">

## Propiedades

-    {{PropertyData | Base}}: El punto base del plano espejo

-    {{PropertyData | Normal}}: la dirección normal del plano reflejado


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Programación

La herramienta de clonación se puede usar en [macros](macros.md) y desde la consola de python usando la siguiente función:


</div>

To mirror objects use the `mirror` method of the Draft module.


```python
mirrored_list = mirror(objlist, p1, p2)
```


<div class="mw-translate-fuzzy">

-   Hace espejo (s) del objeto (s) dado a través de un plano definido por una línea de p1 a p2, y paralelo a la vista actual
-   El resultado es un objeto [Part Mirror](Part_Mirror.md)
-   Si el objeto original cambia, el objeto final también cambia pero se mantiene reflejado


</div>

Ejemplo:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

place = App.Placement(FreeCAD.Vector(1000, 0, 0), App.Rotation())
polygon1 = Draft.make_polygon(3, 750)
polygon2 = Draft.make_polygon(5, 750, placement=place)

p1 = App.Vector(2000, -1000, 0)
p2 = App.Vector(2000, 1000, 0)

line1 = Draft.make_line(p1, p2)
mirrored1 = Draft.mirror(polygon1, p1, p2)

Line2 = Draft.make_line(-p1, -p2)
mirrored2 = Draft.mirror([polygon1, polygon2], -p1, -p2)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Mirror/es
