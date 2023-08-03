---
 GuiCommand:
   Name: Draft WorkingPlaneProxy
   Name/es: Borrador PlanoTrabajoProxy
   MenuLocation: Borrador , Utilidades , Crear proxy del plano trabajo
   Workbenches: Draft_Workbench/es, Arch_Workbench/es
   SeeAlso: Draft_SelectPlane/es
---

# Draft WorkingPlaneProxy/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

Este comando colocará un objeto Proxy de Plano alineado con el actual [Plano trabajo](Draft_SelectPlane/es.md).


</div>

<img alt="" src=images/Draft_WPProxy_example.png  style="width:400px;"> 
*Tres proxies de planos de trabajo que muestran diferentes orientaciones y rellenos*

## Utilización


<div class="mw-translate-fuzzy">

1.  Asegúrate de que el [Plano trabajo](Draft_SelectPlane/es.md) está configurado como quieres.
2.  A continuación, vaya al menú **Borrador → Utilidades → <img src="images/Draft_WorkingPlaneProxy.svg" width=16px> Crear proxy de plano trabajo**.


</div>

## Context menu 

For a Draft WorkingPlaneProxy these additional options are available in the [Tree view](Tree_view.md) context menu:

-    **<img src="images/Draft_SelectPlane.svg" width=16px> Write camera position**: updates the **View Data** property of the working plane proxy with the current [3D view](3D_view.md) camera settings.

-    **<img src="images/Draft_SelectPlane.svg" width=16px> Write objects state**: updates the **Visibility Map** property of the working plane proxy with the current visibility state of objects in the document.

## Notes


<div class="mw-translate-fuzzy">

## Notas

-   El plano de trabajo almacenado en el objeto Proxy puede restaurarse haciendo doble clic en el objeto en la vista de árbol, o seleccionando el objeto Proxy y utilizando el **<img src="images/Draft_SelectPlane.svg" width=16px> [Borrador SeleccionarPlano](Draft_SelectPlane/es.md).**.
-   La posición de la cámara se almacena en el objeto Proxy en el momento de su creación. Esta posición puede actualizarse en cualquier momento: haz zoom, panorámica y rotación de la vista como desees, luego haz clic con el botón derecho en el objeto Proxy en la vista de árbol y selecciona **<img src="images/Draft_SelectPlane.svg" width=16px>. Escribir posición de la cámara**.
-   El estado de visibilidad de todos los objetos también se almacena en el objeto Proxy en el momento de su creación. Este estado puede actualizarse en cualquier momento: establezca la propiedad **Visibility** de los objetos a `True` o `False` según desee, luego haga clic con el botón derecho en el objeto Proxy en la vista de árbol, y seleccione **<img src="images/Draft_SelectPlane.svg" width=16px> Escribir estado de los objetos**.
-   Los proxies de plano pueden moverse y girarse como cualquier otro objeto para que definan el plano de trabajo deseado. Su apariencia visual también se puede cambiar en el [Editor de propiedades](Property_editor/es.md).


</div>

## Propiedades

See also: [Property editor](Property_editor.md).

A Draft WorkingPlaneProxy object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Base}}

-    **Placement|Placement**: specifies the position of the working plane proxy in the [3D view](3D_view.md). See [Placement](Placement.md).

-    **Shape|Shape|Hidden**: specifies the shape of the working plane proxy.

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

## Guión


<div class="mw-translate-fuzzy">


**Ver también:**

[Borrador API](Draft_API/es.md) y [FreeCAD Fundamentos de Guión](FreeCAD_Scripting_Basics/es.md).


</div>


<div class="mw-translate-fuzzy">

Los objetos proxy del plano de trabajo se pueden utilizar en [macros](Macros/es.md) y desde la consola de [Python](Python/es.md) utilizando la siguiente función:


</div>

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


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft WorkingPlaneProxy/es
