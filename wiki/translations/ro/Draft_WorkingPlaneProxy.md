# Draft WorkingPlaneProxy/ro
---
- GuiCommand:   Name:Draft SetWorkingPlaneProxy   Workbenches:[Arch](Draft_Workbench___Draft]],_[[Arch_Workbench.md)|MenuLocation:Draft → Utilities → Create WP Proxy   SeeAlso:[[Draft SelectPlane]]---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Această comandă va plasa un obiect Proxy în document, plasat și aliniat la actualul [ Planul de lucru](Draft_SelectPlane.md). Când se utilizează comanda [Draft SelectPlane](Draft_SelectPlane.md) cu un astfel de obiect Proxy selectat sau prin dublu clic pe el în vizualizarea arborescentă, planul de lucru va fi poziționat și aliniat înapoi cu obiectul proxy. Poziția camerei și starea ascunsă/afișată a obiectelor sunt de asemenea stocate în obiectul Proxy și pot fi restabilite dacă proprietățile corespunzătoare sunt activate (vedeți mai jos).


</div>

<img alt="" src=images/Draft_WPProxy_example.png  style="width:400px;"> 
*Three working plane proxies showing different orientations and offsets*

## Usage


<div class="mw-translate-fuzzy">

## Cum se folosește 

1.  Asigurați-vă că [ Planul de lucru](Draft_SelectPlane.md) este setat așa cum doriți.
2.  Apăsați Draft -\> Utilities -\> **<img src="images/Draft_SetWorkingPlaneProxy.png" width=16px> [Create WP Proxy](Draft_SetWorkingPlaneProxy.md)
**


</div>

## Context menu 

For a Draft WorkingPlaneProxy these additional options are available in the [Tree view](Tree_view.md) context menu:

-    **<img src="images/Draft_SelectPlane.svg" width=16px> Write camera position**: updates the **View Data** property of the working plane proxy with the current [3D view](3D_view.md) camera settings.

-    **<img src="images/Draft_SelectPlane.svg" width=16px> Write objects state**: updates the **Visibility Map** property of the working plane proxy with the current visibility state of objects in the document.

## Notes

-   Working plane proxies can be _ to snap to their **Placement** point.

## Proprietăți

See also: [Property editor](Property_editor.md).

A Draft WorkingPlaneProxy object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Base}}


<div class="mw-translate-fuzzy">

-    {{PropertyData | Placement}}: stochează poziția acestui proxy și planul de lucru corespunzător

-    {{PropertyView | Dimensiune afișare}}: mărimea obiectului Proxy din vizualizarea 3D

-    {{PropertyView | Arrow Size}}: mărimea săgeților de pe cele 3 axe

-    {{PropertyView | Restore View}}: Dacă este adevărat, poziția camerei va fi restabilită la activarea (prin dublu clic sau [Draft SelectPlane](Draft_SelectPlane.md)) acest obiect

-    {{PropertyView | Restore State}}: Dacă este adevărat, starea de vizibilitate a tuturor obiectelor din documentul curent va fi restabilită la activarea (prin dublu-clic sau [Draft SelectPlane](Draft_SelectPlane.md))


</div>

### View


{{TitleProperty|Base}}

-    **Line Color|Color**: specifies the color of all elements of the working plane proxy.

-    **Line Width|Float**: specifies the line width of the axes and arrow symbols.

-    **Restore State|Bool**: specifies if the **Visibility Map** is restored when the [working plane](Draft_SelectPlane.md) is aligned with the working plane proxy.

-    **Restore View|Bool**: specifies if the **View Data** is restored when the [working plane](Draft_SelectPlane.md) is aligned with the working plane proxy.

-    **Transparency|Percent**: specifies the transparency of the face of the working plane proxy.

-    **View Data|FloatList**: specifies the camera position and settings.

-    **Visibility Map|Map|Hidden**: specifies the visibility state of objects.


{{TitleProperty|Draft}}

-    **Arrow Size|Length**: specifies the size of the arrow symbols displayed at the tip of the three axes.

-    **Display Size|Length**: specifies the length and width of the working plane proxy.

## Script-Programare 

Obiectele proxy de lucru de lucru pot fi ușor create în script și [macros](macros.md):

See also: _.

To create a Draft WorkingPlaneProxy use the `make_workingplaneproxy` method of the Draft module.

If the [Draft Workbench](Draft_Workbench.md) is active the FreeCAD application object has a `DraftWorkingPlane` property which stores the current working plane. The {{Incode|Placement}} from the {{Incode|getPlacement}} method of the `DraftWorkingPlane` object can be used to create an aligned working plane proxy. The {{Incode|Placement}} of a working plane proxy in turn can be used to realign the working plane.


```python
# This code only works if the Draft Workbench is active!

import FreeCAD as App
import FreeCADGui as Gui
import Draft

doc = App.newDocument()

workplane = App.DraftWorkingPlane
place = workplane.getPlacement()

proxy = Draft.make_workingplaneproxy(place)
proxy.ViewObject.DisplaySize = 3000
proxy.ViewObject.ArrowSize = 200

axis2 = App.Vector(1, 1, 1)
point2 = App.Vector(3000, 0, 0)
place2 = App.Placement(point2, App.Rotation(axis2, 90))

proxy2 = Draft.make_workingplaneproxy(place2)
proxy2.ViewObject.DisplaySize = 3000
proxy2.ViewObject.ArrowSize = 200

workplane.setFromPlacement(proxy2.Placement, rebase=True)
Gui.Snapper.setGrid()

doc.recompute()
```

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft WorkingPlaneProxy/ro
