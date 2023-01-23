# Part Circle/ro
---
- GuiCommand:   Name:Part Circle   MenuLocation:Part → [Workbenches:[[Part Workbench   Part](Part_CreatePrimitives___Create_Primitives]]_→_Circle.md),  [OpenSCAD](OpenSCAD_Workbench.md)|SeeAlso:..---


</div>




<div class="mw-translate-fuzzy">

## Descriere

Un element primitiv geometric este Circle care este disponibil din dialogul Create Primitives în Atelierul de lucru Part.


</div>


<div class="mw-translate-fuzzy">

Această comandă va crea o muchie curbată circulară. Cu valorile implicite, muchia curbată circulară va fi închisă și, prin urmare, va fi un cerc. Dacă proprietățile Unghi 0 sau Unghi 1 sunt modificate din valorile implicite (0 și 360) marginea va fi o curbă deschisă, un arc de cerc.


</div>

A Part Circle is in fact a closed counterclockwise circular arc, it can be turned into an arc by changing its **Angle1** and/or **Angle2** properties.

<img alt="" src=images/Part_Circle_Example.png  style="width:400px;">

## Usage

See [Part Primitives](Part_Primitives#Usage.md).

A Part Circle can alternatively be created by selecting three points:

1.  In the task panel of the <img alt="" src=images/Part_Primitives.svg  style="width:16px;"> [Part Primitives](Part_Primitives.md) command select the **<img src="images/Part_Circle.svg" width=16px> Circle** option from the dropdown list.
2.  Press the **From three points** button.
3.  Select three vertices in the [3D view](3D_view.md). There is no need to hold down the **Ctrl** key.
4.  A circle is created.
5.  The selected vertices are only used at creation time to calculate the **Radius** and **Placement** of the circle.

## Example

![Part Circle from the scripting example](images/Part_Circle_Scripting_Example.png )

A Part Circle object created with the [scripting example](#Scripting.md) below is shown here.




<div class="mw-translate-fuzzy">

### Proprietăți

Crearea unui cerc sau a unui arc de cerc parametric.

Utilizăm meniul {{KEY/it|<img src="images/Part_CreatePrimitives.png" width=16px> Crea primitive... → Cerchio}}. Și apare o fereastră de dialog. Se deschide un dialog care vă permite să setați:

### Primitive Geometrice 

+++
| ![](images/PartCirclePrimitivesOptions_it.png ) | Cercul                                         |
|                                                                              |                                                |
|                                                                              | #### Parametri                                 |
|                                                                              |                                                |
|                                                                              | -                               |
|                                                                              |     {{Parameter|Raza}}                         |
|                                                                              |                                             |
|                                                                              |                                                |
|                                                                              | -                               |
|                                                                              |     {{Parameter|Unghiul 1}}                    |
|                                                                              |                                             |
|                                                                              |                                                |
|                                                                              | -                               |
|                                                                              |     {{Parameter|Unghiul 2}}                    |
|                                                                              |                                             |
|                                                                              |                                                |
|                                                                              | -                               |
|                                                                              |     {{Parameter|Cerc definit din trei puncte}} |
|                                                                              |                                             |
+++


</div>

See also: [Property editor](Property_editor.md).

A Part Circle object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Attachment}}

The object has the same attachment properties as a [Part Part2DObject](Part_Part2DObject#Data.md).


{{TitleProperty|Base}}


<div class="mw-translate-fuzzy">

-    {{Parameter|Radius}}: raza muchiei curbate (arc or circle)

-    {{Parameter|Angle 0}}: Unghiul de pornire a muchiei curbate, (degrees anti-clockwise), valoara implictă este 0

-    {{Parameter|Angle 1}}: Unghiul de capăt al muchiei curbate, (degrees sens antiorar/trigonometric), valoarea implictă este 360


</div>

## Scripting

See also: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/), [Part scripting](Part_scripting.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

A Part Circle can be created with the {{Incode|addObject()}} method of the document:


```python
circle = FreeCAD.ActiveDocument.addObject("Part::Circle", "myCircle")
```

-   Where {{Incode|"myCircle"}} is the name for the object.
-   The function returns the newly created object.

Example:


```python
import FreeCAD as App

doc = App.activeDocument()

circle = doc.addObject("Part::Circle", "myCircle")
circle.Radius = 10
circle.Angle1 = 45
circle.Angle2 = 225
circle.Placement = App.Placement(App.Vector(1, 2, 3), App.Rotation(30, 45, 10))

doc.recompute()
```





{{Part_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Circle/ro
