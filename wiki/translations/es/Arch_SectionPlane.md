---
- GuiCommand:/es
   Name:Arch SectionPlane
   Name/es:Arch Plano de Sección
   MenuLocation:Arquitectura → Plano de sección
   Workbenches:[Entorno de Arquitectura](Arch_Workbench/es.md)
   Shortcut:**S** **P**
---

# Arch SectionPlane/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

Esta herramienta coloca en el documento actual un gizmo de plano de sección, que define una sección o plano de vista. El gizmo toma su ubicación de acuerdo con el actual [ Draft Working Plane](Draft_SelectPlane.md) y puede reubicarse y reorientarse moviéndolo y girándolo, hasta que describa la vista 2D que desea obtener. El objeto Plano de Sección solo considerará un cierto conjunto de objetos. Los objetos que se seleccionan cuando se crea un plano de sección se agregarán a ese conjunto automáticamente. Posteriormente, se pueden agregar o eliminar otros objetos de un objeto Plano de Sección con las herramientas [Arch Add/es](Arch_Add/es.md) y [Arch Remove/es](Arch_Remove/es.md), o haciendo doble clic en el Plano de sección en la vista de árbol.


</div>


<div class="mw-translate-fuzzy">

El plano de sección por sí solo no creará ninguna vista de sus objetos establecidos. Para eso, debe crear un [ Drawing DraftView](Draft_Drawing/es.md) para crear una vista en un [ Drawing page](Drawing_Workbench/es.md), un [Draft Shape2DView/es](Draft_Shape2DView/es.md) para crear una vista en el documento 3D en sí mismo, o a [ TechDraw ArchView](TechDraw_ArchView/es.md) para crear una vista en un [ TechDraw page](TechDraw_Workbench/es.md).


</div>

<img alt="" src=images/Arch_SectionPlane_example.jpg  style="width:600px;">


<div class="mw-translate-fuzzy">

## Utilización


</div>


<div class="mw-translate-fuzzy">

1.  Opcionalmente, configure el [ Draft Working Plane](Draft_SelectPlane/es.md) para reflejar el plano donde desea colocar el plano de sección
2.  Seleccionar los objetos que quieres incluir en la vista de sección
3.  Presionar el botón <img alt="" src=images/Arch_SectionPlane.png  style="width:16px;"> 
**Plano de sección** o pulsar las teclas **S** y **P**
4.  [ Mover](Draft_Move/es.md) / [ rotar](Draft_Rotate/es.md) el plano de sección en la posición correcta si es necesario
5.  Seleccione el plano de sección si no está seleccionado
6.  Use ya sea [ Drawing DraftView](Draft_Drawing/es.md), [Draft Shape2DView/es](Draft_Shape2DView/es.md) o [ TechDraw ArchView](TechDraw_ArchView/es.md) para crear una vista


</div>

## Opciones


<div class="mw-translate-fuzzy">

-   El objeto de plano de sección solo considerará un cierto conjunto de objetos, no todos los objetos del documento. Los objetos se pueden agregar o eliminar de un objeto SectionPlane utilizando las herramientas [Arch Add/es](Arch_Add/es.md) y [Arch Remove/es](Arch_Remove/es.md), o haciendo doble clic en el Plano de sección en la vista de árbol, seleccionando objetos en la lista de en el Escena 3D, y presionando **agregar** o quitar **botones**.


</div>


<div class="mw-translate-fuzzy">

-   Con un objeto plano de sección seleccionado, utilizar la herramienta [Forma 2D Vista](Draft_Shape2DView/es.md) para crear un objeto forma representando la vista de sección en el documento


</div>

<img alt="" src=images/Arch_Section_example2.jpg  style="width:600px;">


<div class="mw-translate-fuzzy">

-   Crear [ Drawing DraftViews](Draft_Drawing/es.md) si está trabajando con [ Drawing Workbench](Drawing_Workbench/es.md), o [ TechDraw ArchView](TechDraw_ArchView/es.md) si está utilizando [ TechDraw Workbench](TechDraw_Workbench/es.md) .


</div>

<img alt="" src=images/Arch_Section_example3.jpg  style="width:600px;">

-   El plano de sección también se puede usar para mostrar toda la vista 3D cortada por un plano infinito. Esto es solo visual, y no afectará la geometría de los objetos que se cortan.

<img alt="" src=images/Arch_SectionPlane_CutView.jpg  style="width:600px;">

## Propiedades


<div class="mw-translate-fuzzy">

-    {{PropertyData/es | Only Solids}}: si esto es True, no se tendrán en cuenta los objetos no sólidos del conjunto

-    {{PropertyView/es | Display Length}}: la longitud del gizmo del plano de sección en la vista 3D. No afecta la vista resultante

-    {{PropertyView/es | Display Height}}: la altura del gizmo del plano de sección en la vista 3D. No afecta la vista resultante

-    {{PropertyView/es | Tamaño de flecha}}: El tamaño de las flechas del gizmo de plano de sección en la vista 3D. No afecta la vista resultante

-    {{PropertyView/es | Cut View}}: si esto es True, toda la vista 3D se cortará en la ubicación de este plano de sección (experimental).


</div>

<img alt="" src=images/Arch_SectionPlane_ClipView.png  style="width:600px;">



*The Arch SectionPlane with the clip view option will behave like a camera, limiting the field of view.*

## Tweaks

-   Adding manually a property named **RotateSolidRender** of type **App::PropertyAngle** to the section plane\'s **View** properties (right-click the properties view -\> show all, right-click again -\> add property) allows to rotate the render when using Solid mode. This is useful when a rendered view has for example both Arch and Draft elements, and the rendering of the Arch elements is rotated in relation to the Draft elements. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

## Programación


</div>


<div class="mw-translate-fuzzy">

La herramienta plano de sección se puede utilizar en [macros](macros/es.md) y desde la consaola de Python mediante las siguientes funciones:


</div>


```python
Section = makeSectionPlane(objectslist=None, name="Section")
```


<div class="mw-translate-fuzzy">


:   Crea objetos plano de sección incluyendo los objetos dados


</div>

Ejemplo:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseline2 = Draft.makeLine(p1, -1*p2)

Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
Wall2 = Arch.makeWall(baseline2, length=None, width=150, height=1800)
Structure = Arch.makeStructure(length=1000, width=1000, height=200)
FreeCAD.ActiveDocument.recompute()

BuildingPart = Arch.makeBuildingPart([Wall1, Wall2])

Floor = Arch.makeFloor([BuildingPart])
Building = Arch.makeBuilding([Floor, Structure])
Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute()

Section1 = Arch.makeSectionPlane([Wall1, Wall2])
Section2 = Arch.makeSectionPlane([Structure])
Section3 = Arch.makeSectionPlane([Site])
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


</div>







[<img src="images/Property.png" style="width:16px"> Arch/es](<img src="images/Property.png" style="width:16px"> Arch/es.md)

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch SectionPlane/es
